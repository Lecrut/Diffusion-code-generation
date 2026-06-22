class LargeStringAnalyzer:
    FIRST_WORD_INDEX = 0
    LAST_WORD_INDEX = -1

    @staticmethod
    def _validate_input(text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        if not text:
            return []
        return text.split()

    def __init__(self, text):
        self.words = self._validate_input(text)

    def get_first_and_last(self):
        if not self.words:
            return None, None
        first = self.words[self.FIRST_WORD_INDEX]
        last = self.words[self.LAST_WORD_INDEX]
        return first, last

if __name__ == '__main__':
    sample_text = "Performance optimization is critical for large inputs"
    analyzer = LargeStringAnalyzer(sample_text)
    first, last = analyzer.get_first_and_last()
    print(first)
    print(last)