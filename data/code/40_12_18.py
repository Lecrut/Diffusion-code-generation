class FirstLetterExtractor:
    """A class designed to extract first letters from a list of strings."""

    def __init__(self):
        self._data = []

    @staticmethod
    def _get_first_letter(s: str) -> str | None:
        if not s or len(s.strip()) == 0:
            return None
        char = s[0]
        # Ensure we return the character even if it is whitespace by stripping only for logic check, 
        # but actually standard behavior implies taking the literal first unicode codepoint unless specified.
        # Given "first letter", usually implies ignoring leading spaces or just the very first char?
        # Let's assume standard definition: the character at index 0 after removing leading/trailing whitespace is common interpretation for 'letter', 
        # but strictly 'list of strings' might mean literal s[0]. 
        # However, "first letter" usually implies alphabetic. To be safe and robust without over-engineering:
        # We will take the first character that constitutes a word (alphabetic) or just return s.strip()[0] if non-empty?
        # Let's stick to simple logic: Return s[0] if string is not empty, else None. 
        # But "letter" implies alphabetic. Let's assume any unicode char counts as a 'character', but the prompt says "first letter".
        # A safe bet for "First Letter" in English context often ignores case and asks for the character itself.
        return s[0]

    def extract_all(self, strings: list[str]) -> list[str | None]:
        """
        Extracts the first letter from each string in the provided list.
        
        Args:
            strings (list[str]): A list of input strings.
            
        Returns:
            list[str | None]: A list containing the first character of each corresponding non-empty string, 
                            or None for empty/None values if they existed as elements originally intended to be passed.
                            
        Note on 'letter': This implementation returns any single Unicode codepoint found at index 0 of a non-empty string.
                      Empty strings yield None. Leading spaces are preserved per strict indexing unless specified otherwise.
        """
        return [self._get_first_letter(s) for s in strings]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()

    sample_strings = ["Hello", "World", "", "Python ", "!@#", None, "-"]
    
    # Process the sample data
    result_list = extractor.extract_all(sample_strings)
    
    print("Input list:", sample_strings)
    print("Output list:", result_list)