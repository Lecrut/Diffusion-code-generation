class FirstLetterExtractor:
    """A class to extract first letters from a list of strings."""
    
    def __init__(self):
        self._name = "FirstLetterExtractor"

    def _get_first_letter(self, word: str) -> str | None:
        """Extracts the first letter of a non-empty string. Returns None if empty."""
        return word[0] if len(word) > 0 else None

    def extract_all(self, words_list):
        """Returns a list containing the first letter of each string in input."""
        
        result = []
        
        for w in words_list:
            char = self._get_first_letter(w)
            
            # Ensure only characters are added (None is filtered implicitly by type check if needed, but here we add None for empty strings per logic or skip? Task says first letters. Usually implies non-empty input expectation but let's handle gracefully.)
            result.append(char)
        
        return result

if __name__ == '__main__':
    # Hard-coded sample values to ensure no external dependencies or user interaction is required
    samples = [
        "Python", 
        "",             # Edge case: empty string
        "!Hello World!",  # Starts with symbol
        "123 Start"     # Starts with digit
    ]

    extractor_obj = FirstLetterExtractor()
    
    output_list = extractor_obj.extract_all(samples)
    
    print("Extracted first letters:")
    for idx, letter in enumerate(output_list):
        if letter is None:
            print(f"{idx}: <None> (from empty string)")
        else:
            print(f"{idx}: '{letter}'")