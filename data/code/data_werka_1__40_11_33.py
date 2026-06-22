class FirstLetterExtractor:
    def extract_all(self, list_of_strings):
        return [self._get_first_letter(s) for s in list_of_strings if self._is_non_empty(s)]

    def _get_first_letter(self, string):
        return string[0]

    def _is_non_empty(self, string):
        return bool(string)

if __name__ == '__main__':
    SAMPLE_DATA = ["apple", "banana", "cherry", "date"]
    extractor = FirstLetterExtractor()
    result = extractor.extract_all(SAMPLE_DATA)
    print(result)