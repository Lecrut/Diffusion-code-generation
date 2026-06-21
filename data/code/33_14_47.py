class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def remove_spaces(self):
        return self.input_string.replace(' ', '')

if __name__ == '__main__':
    sample_input1 = '  This is   a test string with  spaces  '
    processor1 = StringProcessor(sample_input1)
    result1 = processor1.remove_spaces()
    print(result1)

    sample_input2 = "  Another example with   multiple spaces.  "
    processor2 = StringProcessor(sample_input2)
    result2 = processor2.remove_spaces()
    print(result2)