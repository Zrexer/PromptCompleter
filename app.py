from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion

class CustomCompleter(Completer):
    def get_completions(self, document, complete_event):
        if document.text_before_cursor.endswith('e'):
            yield Completion('xit', -1)
        
        if document.text_before_cursor.endswith('ex'):
            yield Completion('it', -1)

        if document.text_before_cursor.endswith('exi'):
            yield Completion('t', -1)

user_input = prompt('Enter text: ', completer=CustomCompleter())
print('You entered:', user_input)
