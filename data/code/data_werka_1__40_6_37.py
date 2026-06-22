class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def first_letter_of_first_word(self):
        stripped_input = self.input_string.lstrip()
        if ' ' in stripped_input:
            return stripped_input[0]
        elif stripped_input:
            return stripped_input[0]
        else:
            return None

if __name__ == '__main__':
    sample_string = '   Python programming'
    processor = StringProcessor(sample_string)
    print(processor.first_letter_of_first_word())