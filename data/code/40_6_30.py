class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def first_letter_of_first_word(self):
        stripped_string = self.input_string.strip()
        if not stripped_string:
            return None
        first_word_end = stripped_string.find(' ')
        return stripped_string[0] if first_word_end == -1 else stripped_string[0]

if __name__ == '__main__':
    sample_string = '   Test case'
    processor = StringProcessor(sample_string)
    print(processor.first_letter_of_first_word())

    empty_string = ''
    empty_processor = StringProcessor(empty_string)
    print(empty_processor.first_letter_of_first_word())

    single_char_string = ' A'
    single_char_processor = StringProcessor(single_char_string)
    print(single_char_processor.first_letter_of_first_word())