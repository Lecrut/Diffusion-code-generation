class FirstLetterExtractor:
    def __init__(self):
        self._empty_string = ""

    def _is_valid_string(self, s):
        return isinstance(s, str) and s != self._empty_string

    def extract_all(self, strings):
        if not all(isinstance(s, str) for s in strings):
            raise ValueError("All elements must be strings")
        
        first_letters = []
        for s in strings:
            if self._is_valid_string(s):
                first_letters.append(s[0])
        
        return first_letters

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_strings = ["lemon", "mango", "nectarine"]
    print(extractor.extract_all(sample_strings))