class StringProcessor:

    def __init__(self, text):
        self.text = text

    def _strip_leading_spaces(self):
        return self.text.lstrip()

    def first_letter_of_first_word(self):
        stripped_text = self._strip_leading_spaces()
        if ' ' in stripped_text:
            return stripped_text[0]
        else:
            return stripped_text[0] if stripped_text else None
if __name__ == '__main__':
    sample_string1 = '   Greetings'
    sample_string2 = 'Hello there'
    sample_string3 = '   '
    processor1 = StringProcessor(sample_string1)
    print(processor1.first_letter_of_first_word())
    processor2 = StringProcessor(sample_string2)
    print(processor2.first_letter_of_first_word())
    processor3 = StringProcessor(sample_string3)
    print(processor3.first_letter_of_first_word())