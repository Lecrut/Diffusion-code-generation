class StringCleaner:
    """A class to remove all spaces from a given string efficiently."""

    def clean(self, text):
        """
        Remove all space characters (' ') from the input string.
        
        Args:
            text (str): The input string which may contain spaces.
            
        Returns:
            str: A new string with all spaces removed.
            
        Raises:
            TypeError: If the input is not a string.
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected string type, got {type(text).__name__}")

        # Using join on a generator expression is highly optimized in Python 
        # as it avoids creating intermediate list objects and handles edge cases naturally.
        return ''.join(char for char in text if not (char == ' '))

if __name__ == '__main__':
    cleaner = StringCleaner()

    test_cases = [
        "Hello World",
        "",
        "  Multiple   Spaces  ",
        "NoSpacesHere",
        "Café résumé"
    ]

    for text in test_cases:
        result = cleaner.clean(text)
        print(f'Input: "{text}" -> Output: "{result}"')