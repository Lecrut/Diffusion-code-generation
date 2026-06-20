class StringProcessor:
    def __init__(self, text: str):
        self.text = text

    def get_first_letter_of_first_word(self):
        stripped = self.text.lstrip()
        if not stripped:
            return None
        first_word = stripped.split()[0] if stripped.split() else ""
        if not first_word:
            return None
        return first_word[0]

if __name__ == '__main__':
    processor = StringProcessor("  Hello World  ")
    result = processor.get_first_letter_of_first_word()
    print(result)