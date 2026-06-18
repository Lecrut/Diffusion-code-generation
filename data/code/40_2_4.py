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
        if not isinstance(text, str):
            raise TypeError(f"Expected string input, got {type(text).__name__}")

        # Split the text into words based on whitespace and filter out empty strings
        words = [word for word in text.split() if word]
        
        return [word[0].lower() for word in words]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()

    # Hard-coded sample values as per requirements (no user input, args, or network)
    samples = [
        "Hello World",
        "Python Programming is Fun",
        "",
        "   Multiple   Spaces   Here  ",
        "OneTwoThreeFourFive"
    ]

    for text in samples:
        result = extractor.extract(text)
        print(f"Input: '{text}'")
        print(f"Output: {result}")
        print("-" * 20)