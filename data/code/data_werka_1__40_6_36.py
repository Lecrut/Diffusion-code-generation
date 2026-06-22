class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def first_letter_of_first_word(self):
        stripped_string = self.input_string.lstrip()
        if ' ' in stripped_string:
            return stripped_string[0]
        else:
            return stripped_string[0] if stripped_string else None

if __name__ == '__main__':
    SAMPLE_STRING_1 = '   Hello world'
    SAMPLE_STRING_2 = '   Example text'
    SAMPLE_STRING_3 = '   Hello World'

    processor1 = StringProcessor(SAMPLE_STRING_1)
    print(processor1.first_letter_of_first_word())

    processor2 = StringProcessor(SAMPLE_STRING_2)
    print(processor2.first_letter_of_first_word())

    processor3 = StringProcessor(SAMPLE_STRING_3)
    print(processor3.first_letter_of_first_word())