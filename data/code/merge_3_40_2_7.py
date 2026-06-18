class FirstLetterExtractor:
    """A class that extracts the first letter of every word from a given text."""

    def extract(self, text: str) -> list[str]:
        """
        Returns a list containing the first letter of each word in the input text.
        
        Words are defined as sequences of alphabetic characters separated by non-alphabetic 
        characters (spaces, punctuation, etc.). The method handles mixed case and ignores 
        empty strings or inputs with no words.

        Args:
            text (str): The input string to process.

        Returns:
            list[str]: A list of single-character strings representing the first letter 
                      of each word found in the input text.
        """
        if not isinstance(text, str) or not text.strip():
            return []

        # Split by non-alphabetic characters and filter out empty segments
        words = [word for word in re.split(r'[^a-zA-Z]+', text) if len(word) > 0]
        
        return [word[0].lower() for word in words]

import re

if __name__ == '__main__':
    # Hard-coded sample values to test the class functionality without user input.
    extractor = FirstLetterExtractor()
    
    samples = [
        "Hello, World!",
        "Python is awesome.",
        "",
        "   ",
        "One two three four five",
        "!@#$%^&*()"
    ]

    for sample in samples:
        result = extractor.extract(sample)
        print(f"Input: '{sample}'")
        print(f"Output: {result}")
        print("-" * 20)