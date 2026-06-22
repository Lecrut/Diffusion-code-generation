class StringProcessor:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        self.input_string = input_string

    def first_letter_of_first_word(self):
        stripped_string = self.input_string.lstrip()
        try:
            return stripped_string[0]
        except IndexError:
            return None

if __name__ == '__main__':
    sample_string = '   Welcome to the jungle'
    processor = StringProcessor(sample_string)
    print(processor.first_letter_of_first_word())