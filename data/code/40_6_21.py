class StringProcessor:
    def __init__(self, text):
        self.text = text

    def get_first_letter_of_first_word(self):
        trimmed_text = self.text.lstrip()
        if not trimmed_text:
            return None
        first_char = trimmed_text[0]
        if first_char.isalpha():
            return first_char
        return None

if __name__ == '__main__':
    sample_string = "   Hello World"
    processor = StringProcessor(sample_string)
    result = processor.get_first_letter_of_first_word()
    print(result)