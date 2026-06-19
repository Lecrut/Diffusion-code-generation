class FirstLetterExtractor:
    def extract_all(self, list_of_strings):
        if not isinstance(list_of_strings, list):
            raise ValueError("Input must be a list")
        return [self._get_first_letter(s) for s in list_of_strings]

    def _get_first_letter(self, string):
        if not isinstance(string, str) or not string:
            raise ValueError("Each item must be a non-empty string")
        return string[0]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    extractor = FirstLetterExtractor()
    result = extractor.extract_all(sample_list)
    print(result)