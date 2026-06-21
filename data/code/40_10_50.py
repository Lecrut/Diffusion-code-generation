class FirstLetterExtractor:
    _VALID_TYPE = str

    @staticmethod
    def _is_valid_string(s):
        return isinstance(s, FirstLetterExtractor._VALID_TYPE) and s

    def extract_all(self, strings):
        if not all(isinstance(s, FirstLetterExtractor._VALID_TYPE) for s in strings):
            raise ValueError("All elements must be strings")
        return [s[0] for s in strings if FirstLetterExtractor._is_valid_string(s)]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_strings = ["lemon", "mango", "nectarine"]
    print(extractor.extract_all(sample_strings))