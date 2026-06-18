class FirstLetterExtractor:
    """A class designed to extract first letters from a list of strings."""

    def __init__(self):
        self._extracted_letters = []

    def _get_first_letter(self, string):
        """Helper method to get the first letter from a given string.
        
        Args:
            string (str): The input string.
            
        Returns:
            str or None: The first character if present, otherwise None.
        """
        return string[0] if len(string) > 0 else ''

if __name__ == '__main__':
    pass
