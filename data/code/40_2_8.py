import re

class FirstLetterExtractor:
    """A class that extracts the first letter of every word from a given text."""

    def extract(self, text: str) -> list[str]:
        """
        Extracts and returns the first letter of each word in the input text.

        The method is case-sensitive but considers only alphabetic characters 
        as valid letters to be included (ignoring digits or symbols attached to words).
        
        Args:
            text (str): The input string containing words to process.
            
        Returns:
            list[str]: A list of strings, where each element is the first letter 
                      found in a word of the original text. Words are separated by non-alphabetic characters.

        Example:
            >>> extractor = FirstLetterExtractor()
            >>> result = extractor.extract("Hello world! Python3.")
            ['H', 'w', 'P']
        """
        
        # Find all maximal contiguous sequences of alphabetic letters in the text
        words_with_leading_letters = re.findall(r'\b[A-Za-z][A-Za-z]*', text)

        return [word[0] for word in words_with_leading_letters if len(word) > 0]

if __name__ == '__main__':
    # Hard-coded sample values as per instructions. No user input or external dependencies.
    
    extractor = FirstLetterExtractor()
    
    test_cases = {
        "Hello world! Python3.", 
        "The quick brown fox jumps over the lazy dog",
        "ABC123DEF xyz_789GHI"
    }

    for text in test_cases:
        result = extractor.extract(text)
        print(f'Input: "{text}"')
        print(f'Output: {result}')