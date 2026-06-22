import re

class WhitespaceRemover:
    def __init__(self):
        self.pattern = re.compile(r'\s+')

    def remove_whitespace(self, input_string):
        return self.pattern.sub('', input_string)

if __name__ == '__main__':
    sample_input = "  This is a   test string with \t various \n whitespace characters.  "
    remover = WhitespaceRemover()
    result = remover.remove_whitespace(sample_input)
    print(result)