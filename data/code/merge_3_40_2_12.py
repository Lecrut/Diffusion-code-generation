class FirstLetterExtractor:
    """A class that extracts the first letter of every word from a given text."""

    def extract(self, text: str) -> list[str]:
        """
        Returns a list containing the first letter of each word in the input text.

        Args:
            text (str): The input string to process.

        Returns:
            List[str]: A list where each element is the first character 
                       of a word found in the input text, preserving order.
        
        Example:
            >>> extractor = FirstLetterExtractor()
            >>> result = extractor.extract("Hello world")
            ['H', 'w']
        """
        # Split the text into words based on whitespace and filter out empty strings
        words = [word for word in text.split()]
        
        if not words:
            return []

        # Extract the first character from each non-empty word
        extracted_letters = [word[0] for word in words if len(word) > 0]
        
        return extracted_letters

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    
    sample_texts = [
        "Hello world",
        "Python programming is fun",
        "",
        "A quick brown fox jumps over the lazy dog"
    ]

    for text in sample_texts:
        result = extractor.extract(text)
        print(f'Input: "{text}"')
        print(f'Output: {result}')
        print()