class StringCleaner:
    """A class to clean strings by removing all spaces."""

    def clean(self, text):
        """
        Remove all space characters from the input string efficiently.

        Args:
            text (str): The input string that may contain spaces.

        Returns:
            str: A new string with all spaces removed.
        
        Examples:
            >>> cleaner = StringCleaner()
            >>> cleaner.clean("Hello World")
            ' HelloWorld' -> 'HellWorld'
        """
        # Using replace is efficient and readable for removing a single character type in Python
        return text.replace(' ', '')

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [
        "Hello World",
        "",
        "  Leading spaces   ",
        "NoSpacesHereAtAll",
        "Multiple   Spaces   InBetween"
    ]

    cleaner = StringCleaner()

    for text in samples:
        cleaned_text = cleaner.clean(text)
        print(f'Input: "{text}" -> Output: "{cleaned_text}"')