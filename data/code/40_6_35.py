class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    @staticmethod
    def _strip_leading_spaces(text):
        return text.lstrip()

    @staticmethod
    def _find_first_space_index(text):
        return text.find(' ')

    def first_letter_of_first_word(self):
        stripped_text = self._strip_leading_spaces(self.input_string)
        first_space_index = self._find_first_space_index(stripped_text)
        if first_space_index == -1:
            return stripped_text[0] if stripped_text else None
        else:
            return stripped_text[0]

if __name__ == '__main__':
    sample_string = '   Python programming'
    processor = StringProcessor(sample_string)
    print(processor.first_letter_of_first_word())