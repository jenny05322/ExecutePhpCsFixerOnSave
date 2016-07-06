import sublime, sublime_plugin, re

class ExecutePhpCsFixerOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):
        if re.search('^.*\.php$', view.file_name()):
            view.window().run_command('exec', {
                'shell_cmd': 'php-cs-fixer fix "' + view.file_name() + '" --level=psr2'
            })
