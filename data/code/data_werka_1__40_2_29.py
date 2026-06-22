class FirstLetterExtractor:
    DELIMITER = ' '

    @staticmethod
    def _split_text(text):
        return text.split(FirstLetterExtractor.DELIMITER)

    @staticmethod
    def _extract_first_letters(words):
        return [word[0] for word in words if word]

    def extract(self, text):
        words = self._split_text(text)
        first_letters = self._extract_first_letters(words)
        return ''.join(first_letters)

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_text = "A unique implementation with class constants and static methods"
    result = extractor.extract(sample_text)
    print(result)