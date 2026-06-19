class FirstLetterExtractor:
    DEFAULT_SAMPLE = ["apple", "banana", "cherry", "date"]

    @staticmethod
    def _extract_first_letter(word):
        return word[0] if word else None

    def extract_all(self, list_of_strings):
        return [self._extract_first_letter(s) for s in list_of_strings]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_list = ["apple", "banana", "cherry", "date"]
    result = extractor.extract_all(sample_list)
    print(result)