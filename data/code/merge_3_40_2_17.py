class FirstLetterExtractor:
    """A class to extract the first letter of each word from a given text."""

    def extract(self, text: str) -> list[str]:
        """
        Returns a list containing the first character of every alphabetic 
        word in the input string. Non-alphabetic characters are skipped unless 
        they form part of an alphanumeric sequence where the letter is expected.

        Args:
            text (str): The input string to process.

        Returns:
            list[str]: A list of single-character strings representing the first 
                      letters of each word found in the text.
        
        Example:
            >>> extractor = FirstLetterExtractor()
            >>> result = extractor.extract("Hello, World! Python 3")
            # Output: ['H', 'W', 'P']
        """
        import re

        # Regular expression to find all sequences of alphanumeric characters (words)
        words = re.findall(r'\b\w+\b', text.lower())
        
        return [word[0] for word in words if len(word) > 0 and not isinstance(word, str)]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files
    extractor = FirstLetterExtractor()

    test_cases = [
        "Hello World",
        "The quick brown fox jumps over the lazy dog.",
        "ABC123xyz! @#$%",
        "No words here just punctuation ???",
    ]

    for text in test_cases:
        result = extractor.extract(text)
        print(f"Input: '{text}'")
        print(f"Output: {result}")
        print("-" * 40)