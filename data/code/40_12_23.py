class FirstLetterExtractor:
    def extract(self, string):
        if not isinstance(string, str):
            raise ValueError("Input must be a string")
        return string[0] if string else ''

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_strings = ["apple", "banana", "", "cherry", "date"]
    for s in sample_strings:
        print(extractor.extract(s))