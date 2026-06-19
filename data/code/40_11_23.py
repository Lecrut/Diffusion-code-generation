class FirstLetterExtractor:
    def extract_all(self, list_of_strings):
        return [self._get_first_letter(s) for s in list_of_strings]

    def _get_first_letter(self, string):
        if not string:
            return None
        return string[0]

if __name__ == '__main__':
    sample_list = ["grape", "honeydew", "kiwi", "lemon"]
    extractor = FirstLetterExtractor()
    result = extractor.extract_all(sample_list)
    print(result)