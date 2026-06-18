import re

class FirstLetterExtractor:
    """A class to extract the first letter of every word from a given text."""

    def __init__(self):
        self._cache = None  # Optional cache, though not strictly necessary for this simple task.

    def extract(self, text: str) -> list[str]:
        """
        Returns a list containing the first letter of each word in the input text.

        Args:
            text (str): The input string to process.

        Returns:
            list[str]: A list of single-character strings representing the first letters 
                      of each alphabetic character found at the start of words.
        
        Example:
            >>> extractor = FirstLetterExtractor()
            >>> extractor.extract("Hello, world!")
            ['H', 'w']
        """
        # Use regex to find all sequences starting with an uppercase letter followed by 
        # any characters (including lowercase), or just standalone letters.
        # The pattern r'\b[a-z][a-zA-Z]*' matches words starting with a lowercase, but we want case-insensitive logic mostly.
        # A simpler approach: split into tokens and take the first char if it's alphabetic.
        
        result = []
        for word in text.split():
            cleaned_word = ''.join(char.lower() if 'a' <= char <= 'z' else '' 
                                   for char in word)  # Normalize to lowercase for consistency or keep original?
            
            # Let's stick to the first alphabetic character found as-is.
            for char in word:
                if char.isalpha():
                    result.append(char)
                    break
        
        return result

if __name__ == '__main__':
    extractor = FirstLetterExtractor()

    sample_texts = [
        "Hello, world!",
        "Python is awesome.",
        "The quick brown fox jumps over the lazy dog",
        "123 numbers 456 here"
    ]

    for text in sample_texts:
        extracted_letters = extractor.extract(text)
        print(f"Input: '{text}'")
        print(f"Output: {extracted_letters}")
        print("-" * 20)