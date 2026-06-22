class FirstLetterExtractor:
    def __init__(self):
        self._valid_types = (str,)
    
    def _validate_input(self, strings):
        if not isinstance(strings, list):
            raise ValueError("Input must be a list.")
        if not all(isinstance(s, self._valid_types) for s in strings):
            raise ValueError("All elements in the list must be strings.")
        if any(len(s) == 0 for s in strings):
            raise ValueError("No empty strings are allowed.")
    
    def extract_all(self, strings):
        self._validate_input(strings)
        return [s[0] for s in strings]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    sample_strings = ["mango", "nectarine", "orange"]
    print(extractor.extract_all(sample_strings))