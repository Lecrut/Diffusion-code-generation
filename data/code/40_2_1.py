class FirstLetterExtractor:
    """A class that extracts the first letter of every word from a given text."""

    def extract(self, text: str) -> list[str]:
        """
        Returns a list containing the first letter of each word in the input text.

        Args:
            text (str): The input string to process.

        Returns:
            List[str]: A list of single-character strings representing 
                       the first letters of each word found in the text.
        
        Example:
            >>> extractor = FirstLetterExtractor()
            >>> result = extractor.extract("Hello world")
            ['H', 'w']
        """
        # Split the text into words based on whitespace and filter out empty strings
        words = [word for word in text.split()]
        
        # Extract the first character from each non-empty word
        return [word[0] if len(word) > 0 else '' for word in words]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()

    sample_texts = [
        "Hello world",
        "Python is great and fun!",
        "",
        "A B C D E"
    ]

    print("First Letter Extraction Results:")
    for text in sample_texts:
        result = extractor.extract(text)
        print(f'Input: "{text}" -> Output: {result}')