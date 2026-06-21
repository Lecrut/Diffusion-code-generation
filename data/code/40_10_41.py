class FirstLetterExtractor:
    def extract_all(self, strings):
        if not all(isinstance(s, str) for s in strings):
            raise ValueError("All elements in the list must be strings.")
        return [s[0] for s in strings if s]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_strings = ["apple", "banana", "cherry"]
    print(extractor.extract_all(sample_strings))