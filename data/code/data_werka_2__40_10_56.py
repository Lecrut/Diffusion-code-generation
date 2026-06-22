class FirstLetterExtractor:
    def __init__(self):
        self._valid_type = str

    def _is_valid_string(self, s):
        return isinstance(s, self._valid_type)

    def extract_all(self, strings):
        if not all(self._is_valid_string(s) for s in strings):
            raise ValueError("All elements must be strings")
        return [s[0] for s in strings if s]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_strings = ["lemon", "mango", "nectarine"]
    result = extractor.extract_all(sample_strings)
    print(result)