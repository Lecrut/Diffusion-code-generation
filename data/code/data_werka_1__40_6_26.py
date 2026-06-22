class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    @staticmethod
    def _is_whitespace(char):
        return char.isspace()

    def first_letter_of_first_word(self):
        stripped_string = ''.join(filter(lambda x: not self._is_whitespace(x), self.input_string))
        if not stripped_string:
            return None
        return stripped_string[0]

if __name__ == '__main__':
    sample_string = '   Another example'
    processor = StringProcessor(sample_string)
    print(processor.first_letter_of_first_word())