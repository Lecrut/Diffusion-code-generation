class FirstLetterExtractor:
    def __init__(self):
        self._empty_string = ""

    def _is_valid_string(self, s):
        return isinstance(s, str) and s != self._empty_string

    def extract_all(self, strings):
        if not all(isinstance(s, str) for s in strings):
            raise ValueError("All elements must be strings")
        return [s[0] for s in strings if self._is_valid_string(s)]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_strings1 = ["apple", "banana", "cherry"]
    print(extractor.extract_all(sample_strings1))

    sample_strings2 = ["dog", "", "frog"]
    print(extractor.extract_all(sample_strings2))

    sample_strings3 = ["grape", "honeydew", ""]
    print(extractor.extract_all(sample_strings3))