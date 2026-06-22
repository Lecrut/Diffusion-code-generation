class FirstLetterExtractor:
    DEFAULT_LIST = ["apple", "banana", "cherry", "date"]

    def extract_all(self, words):
        return [self._get_first_letter(word) for word in words if word]

    @staticmethod
    def _get_first_letter(word):
        return word[0]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_words = ["dog", "elephant", "frog", "giraffe"]
    result = extractor.extract_all(sample_words)
    print(result)