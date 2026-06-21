class WhitespaceRemover:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        self.input_string = input_string

    def remove_whitespace(self):
        return ''.join(self.input_string.split())

if __name__ == '__main__':
    sample_input1 = "  This is a   test string with \t various \n whitespace characters.  "
    remover1 = WhitespaceRemover(sample_input1)
    result1 = remover1.remove_whitespace()
    print(result1)

    sample_input2 = "  Another example \t\n with different whitespaces.  "
    remover2 = WhitespaceRemover(sample_input2)
    result2 = remover2.remove_whitespace()
    print(result2)