class FirstLetterExtractor:
    def __init__(self):
        self.sample_strings = ["apple", "banana", "cherry", "", "date"]

    def extract_first_letter(self, s):
        return s[0] if s else ''

    def extract_all(self):
        first_letters = [self.extract_first_letter(s) for s in self.sample_strings]
        return first_letters

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    result = extractor.extract_all()
    print(result)