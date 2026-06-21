class FirstLetterExtractor:
    def __init__(self):
        self._STRING_TYPE = str

    def _is_valid_string(self, item):
        return isinstance(item, self._STRING_TYPE)

    def extract_all(self, strings):
        if not all(self._is_valid_string(s) for s in strings):
            raise ValueError("All elements must be strings")
        return [s[0] for s in strings if s]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_strings = ["lemon", "mango", "nectarine"]
    print(extractor.extract_all(sample_strings))