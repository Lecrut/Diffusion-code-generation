class FirstLetterExtractor:
    def extract_all(self, strings):
        return [s[0] for s in strings if s]

if __name__ == '__main__':
    sample_strings = ["kiwi", "lemon", "mango"]
    extractor = FirstLetterExtractor()
    result = extractor.extract_all(sample_strings)
    print(result)