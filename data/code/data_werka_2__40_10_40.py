class FirstLetterExtractor:
    def __init__(self):
        self._valid_types = (str,)
    
    def _validate_input(self, strings):
        if not all(isinstance(s, self._valid_types) for s in strings):
            raise ValueError("All elements must be strings")
    
    def extract_all(self, strings):
        self._validate_input(strings)
        return [s[0] for s in strings if s]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_strings = ["grape", "honeydew", "kiwi"]
    print(extractor.extract_all(sample_strings))