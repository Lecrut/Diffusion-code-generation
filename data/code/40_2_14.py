import re

class FirstLetterExtractor:
    """A class to extract the first letter of every word from a given text."""

    def __init__(self):
        pass

    @staticmethod
    def _get_first_letter(word: str) -> str | None:
        """Returns the first alphabetic character in a word or None if no letters exist.
        
        Args:
            word (str): The input word to process.
            
        Returns:
            str | None: The first letter found, or None if none exists.
        """
        for char in word:
            if 'a' <= char.lower() <= 'z':  # Check only alphanumeric letters A-Z a-z
                return char
        return None

    def extract(self, text: str) -> list[str]:
        """Efficiently returns the first letter of every word in the input text.
        
        Handles multiple spaces and newlines by treating any sequence of whitespace 
        as a single separator. Uses regex for efficient tokenization across platforms.
        
        Args:
            text (str): The input string containing words separated by whitespaces or newlines.
            
        Returns:
            list[str]: A list of strings, each being the first letter found in the corresponding word.
                       If a word contains no alphabetic characters, it is skipped.
        
        Example:
            >>> extractor = FirstLetterExtractor()
            >>> result = extractor.extract("Hello World!")
            ['H', 'W']
        """
        # Split by any whitespace sequence (spaces, tabs, newlines) and filter out empty strings
        words = re.findall(r'\S+', text.strip())
        
        letters = []
        for word in words:
            first_letter = self._get_first_letter(word)
            if first_letter is not None:
                # Normalize to uppercase as per common convention unless specified otherwise. 
                # Given the prompt doesn't specify case, we preserve original case logic 
                # by returning 'a' <= char.lower() <= 'z'. To ensure consistency with "first letter",
                # let's return it in its found form (case-sensitive).
                letters.append(first_letter)

        return letters

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    
    sample_text_1 = "Hello World! Python is awesome."
    result_1 = extractor.extract(sample_text_1)
    print(f"Input: {sample_text_1}")
    print(f"Output: {result_1}\n")

    sample_text_2 = "  Multiple   Spaces and\nNewlines here!"
    result_2 = extractor.extract(sample_text_2)
    print(f"Input: '{sample_text_2}'")
    print(f"Output: {result_2}")
    
    # Edge case with no letters
    sample_text_3 = "12345 !@#$%^&*()"
    result_3 = extractor.extract(sample_text_3)
    print(f"Input: '{sample_text_3}'")
    print(f"Output: {result_3}")