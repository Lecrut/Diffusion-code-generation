class WordLengthProcessor:
    def __init__(self):
        self.word_lengths = {}

    def process_text(self, text: str) -> None:
        words = text.split()
        for word in words:
            length = len(word)
            if length not in self.word_lengths:
                self.word_lengths[length] = []
            self.word_lengths[length].append(word)

    def get_word_lengths(self) -> dict[int, list[str]]:
        return self.word_lengths

if __name__ == '__main__':
    processor = WordLengthProcessor()
    sample_text = "Hello world! This is a test, how are you?"
    processor.process_text(sample_text)
    result = processor.get_word_lengths()
    print(f"Output: {result}")