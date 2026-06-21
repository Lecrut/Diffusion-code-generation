class FirstLetterExtractor:
    def __init__(self):
        self._STRING_TYPE = str

    def _is_valid_string(self, s):
        return isinstance(s, self._STRING_TYPE) and s

    def extract_all(self, strings):
        if not all(isinstance(s, self._STRING_TYPE) for s in strings):
            raise ValueError("All elements must be strings")
        return [s[0] for s in strings if self._is_valid_string(s)]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_strings = ["lemon", "mango", "nectarine"]
    print(extractor.extract_all(sample_strings))