class FirstLetterExtractor:
    @staticmethod
    def _get_first_letter(word):
        return word[0] if word else None

    def extract_all(self, list_of_strings):
        return [self._get_first_letter(s) for s in list_of_strings]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    extractor = FirstLetterExtractor()
    result = extractor.extract_all(sample_list)
    print(result)