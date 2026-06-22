class FirstLetterExtractor:
    def extract_all(self, list_of_strings):
        return [self._get_first_letter(s) for s in list_of_strings if s]

    def _get_first_letter(self, string):
        return string[0]

if __name__ == '__main__':
    SAMPLE_DATA = ["hippo", "iguana", "jackal", "kangaroo"]
    extractor = FirstLetterExtractor()
    result = extractor.extract_all(SAMPLE_DATA)
    print(result)