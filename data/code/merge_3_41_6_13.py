class StringCaseManipulator:
    """A class to efficiently manipulate string cases."""

    def to_lower(self, text: str) -> str:
        """Converts a string to lowercase."""
        return text.lower() if isinstance(text, str) else ""

    def to_upper(self, text: str) -> str:
        """Converts a string to uppercase."""
        return text.upper() if isinstance(text, str) else ""

    def to_title(self, text: str) -> str:
        """Converts the first character of each word to uppercase and the rest to lowercase."""
        return text.title() if isinstance(text, str) else ""

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    test_strings = [
        "hello world",
        "HELLO WORLD",
        "Hello World"
    ]

    manipulator = StringCaseManipulator()

    print("Original Strings:")
    for s in test_strings:
        print(f"'{s}'")

    print("\nTransformed Cases:")
    for original in test_strings:
        lower_result = manipulator.to_lower(original)
        upper_result = manipulator.to_upper(original)
        title_result = manipulator.to_title(original)
        
        # Print results with a clear separator to avoid confusion between outputs of different methods.
        print(f"Original: '{original}'")
        print(f"  Lowercase : '{lower_result}'")
        print(f"  Uppercase : '{upper_result}'")
        print(f"  Title     : '{title_result}'")