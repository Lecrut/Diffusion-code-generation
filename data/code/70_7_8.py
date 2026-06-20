class StringProcessor:
    def __init__(self, text):
        self.text = text

    def split_into_words(self):
        return self.text.split()

    def get_first_last_word(self):
        words = self.split_into_words()
        if not words or len(words) < 2:
            raise ValueError("Text must contain at least two words.")
        return words[0], words[-1]

if __name__ == '__main__':
    processor = StringProcessor("Hello, World! This is a test.")
    try:
        first, last = processor.get_first_last_word()
        print(f"First word: {first}, Last word: {last}")
    except ValueError as e:
        print(e)