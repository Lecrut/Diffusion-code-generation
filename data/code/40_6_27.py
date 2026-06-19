class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def first_letter_of_first_word(self):
        stripped_string = self.input_string.lstrip()
        if ' ' in stripped_string:
            return stripped_string[0]
        elif stripped_string:
            return stripped_string[0]
        else:
            return None

if __name__ == '__main__':
    SAMPLE_STRING = '   Welcome to the jungle'
    processor = StringProcessor(SAMPLE_STRING)
    print(processor.first_letter_of_first_word())