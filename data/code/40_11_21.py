class FirstLetterExtractor:
    def extract_all(self, strings):
        return [s[0] for s in strings if s]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_strings = ['apple', 'banana', 'cherry']
    result = extractor.extract_all(sample_strings)
    print(result)