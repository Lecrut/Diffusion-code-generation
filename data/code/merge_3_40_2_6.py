class FirstLetterExtractor:
    """A class to extract the first letter of each word from a given text."""

    def __init__(self):
        pass

    def extract(self, text: str) -> list[str]:
        """
        Returns a list containing the first letter of every word in the input text.

        Args:
            text (str): The input string to process.

        Returns:
            list[str]: A list of single-character strings representing 
                       the first letters of each word found in the text.
        
        Example:
            >>> extractor = FirstLetterExtractor()
            >>> result = extractor.extract("Hello world")
            ['H', 'w']
        """
        # Split the text into words based on whitespace and filter out empty strings if any occur due to multiple spaces
        words = [word for word in text.split()]
        
        return [word[0] if len(word) > 0 else '' for word in words]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network access)
    extractor = FirstLetterExtractor()

    test_cases = [
        "Hello world",
        "Python is great!",
        "",
        "   multiple      spaces  ",
        "A"
    ]

    for text in test_cases:
        result = extractor.extract(text)
        print(f'Input: "{text}" -> Output: {result}')