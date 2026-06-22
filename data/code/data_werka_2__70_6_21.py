class WordExtractor:
    def __init__(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        self._raw_text = text
        self._words = None

    def _get_words(self):
        if self._words is None:
            self._words = self._raw_text.split()
        return self._words

    def get_first(self):
        words = self._get_words()
        if not words:
            return None
        return words[0]

    def get_last(self):
        words = self._get_words()
        if not words:
            return None
        return words[-1]

    def get_word_count(self):
        return len(self._get_words())

    def summary(self):
        words = self._get_words()
        if not words:
            return "Empty string"
        return f"Start: '{words[0]}', End: '{words[-1]}', Count: {len(words)}"

if __name__ == '__main__':
    sample_text = "Performance optimization is critical for large inputs and complex data structures"
    extractor = WordExtractor(sample_text)
    print(extractor.get_first())
    print(extractor.get_last())
    print(extractor.get_word_count())
    print(extractor.summary())