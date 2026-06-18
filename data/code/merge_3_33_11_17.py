class StringCleaner:
    """A class to clean strings by removing all spaces."""

    def clean(self, text: str) -> str:
        """
        Removes all space characters from the input string efficiently.

        Args:
            text (str): The input string containing potential whitespace.

        Returns:
            str: A new string with all spaces removed.
        
        Raises:
            TypeError: If the input is not a string.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        
        # Using replace() which is implemented in C and highly optimized for this operation
        return text.replace(' ', '')

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        "Hello World",
        "",
        "No spaces here!",
        "Multiple   Spaces  And\tTabs",
        "Special chars: a b c d e f g h i j k l m n o p q r s t u v w x y z"
    ]

    cleaner = StringCleaner()

    for test_input in test_cases:
        result = cleaner.clean(test_input)
        print(f'Input:  "{test_input}"')
        print(f'Output: "{result}"\n')