class FirstLetterExtractor:
    EMPTY_STRING = ''

    @staticmethod
    def extract_first_letter(s):
        return s[0] if s else FirstLetterExtractor.EMPTY_STRING

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "", "cherry", "date"]
    extractor = FirstLetterExtractor()
    results = [extractor.extract_first_letter(s) for s in sample_strings]
    print(results)