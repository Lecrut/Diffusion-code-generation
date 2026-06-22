class WhitespaceRemover:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        self.input_string = input_string

    def remove_whitespace(self):
        return ''.join(self.input_string.split())

if __name__ == '__main__':
    sample_input = "  This is a   test string with \t various \n whitespace characters.  "
    remover = WhitespaceRemover(sample_input)
    result = remover.remove_whitespace()
    print(result)