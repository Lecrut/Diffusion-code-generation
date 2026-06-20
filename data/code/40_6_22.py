class StringProcessor:
    def __init__(self, text):
        self.text = text

    def first_letter_of_first_word(self):
        stripped = self.text.lstrip()
        if not stripped:
            return None
        return stripped[0]

if __name__ == '__main__':
    processor = StringProcessor("  Hello world")
    print(processor.first_letter_of_first_word())