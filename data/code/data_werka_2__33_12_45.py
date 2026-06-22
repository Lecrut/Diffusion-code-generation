class WhitespaceRemover:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        self.input_string = input_string

    def remove_whitespace(self):
        return ''.join(self.input_string.split())

if __name__ == '__main__':
    sample_input_1 = "  This is a   test string with \t various \n whitespace characters.  "
    remover_1 = WhitespaceRemover(sample_input_1)
    result_1 = remover_1.remove_whitespace()
    print(result_1)

    sample_input_2 = "Another example with \t different\nwhitespace."
    remover_2 = WhitespaceRemover(sample_input_2)
    result_2 = remover_2.remove_whitespace()
    print(result_2)