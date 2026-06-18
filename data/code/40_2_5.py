class FirstLetterExtractor:
    """A class that extracts the first letter of each word from a given text."""
    
    def extract(self, text: str) -> list[str]:
        """
        Returns a list containing the first letter of every alphabetic 
        character found in words within the input text.
        
        Args:
            text (str): The input string to process.
            
        Returns:
            list[str]: A list of single-character strings representing 
                      the first letters of each word, preserving case.
                      
        Examples:
            >>> extractor = FirstLetterExtractor()
            >>> extractor.extract("Hello world")
            ['H', 'w']
            >>> extractor.extract("PYTHON is great!")
            ['P', 'Y', 'T', 'O', 'N', 'i', 'g'], but words are split by whitespace.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")

        # Split the text into words based on any non-alphabetic character separator 
        # to ensure punctuation attached to words doesn't affect extraction logic improperly,
        # though standard word splitting usually handles this. We use regex for robustness.
        import re
        
        matches = list(set(filter(str.isalpha, re.findall(r'[a-zA-Z]', text))))

        return matches

if __name__ == '__main__':
    extractor = FirstLetterExtractor()

    # Hard-coded sample values to test functionality without user input or files
    samples: dict[str, str] = {
        "simple sentence": "Hello world",
        "multiple words": "Python programming is fun and easy",
        "with punctuation": "It's a beautiful day!",
        "no_letters": "123 numbers only!!!",
        "mixed case": "The Quick Brown Fox Jumps Over The Lazy Dog"
    }

    for test_input, expected_desc in samples.items():
        result = extractor.extract(test_input)
        print(f"{test_input}: {result}")