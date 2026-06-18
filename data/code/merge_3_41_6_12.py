class StringCaseManipulator:
    """A class to efficiently manipulate string cases."""

    def lower(self, text: str) -> str:
        """Convert all characters in the string to lowercase."""
        return text.lower()

    def upper(self, text: str) -> str:
        """Convert all characters in the string to uppercase."""
        return text.upper()

    def title(self, text: str) -> str:
        """Capitalize each word in the string (Title Case)."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        
        # Split into words, capitalize first letter of each, and join back.
        return " ".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    sample_text = "hello world this is a test"

    manipulator = StringCaseManipulator()

    # Demonstrate all three methods with the same input string
    result_lower = manipulator.lower(sample_text)
    print(f"Lowercase: {result_lower}")

    result_upper = manipulator.upper(sample_text)
    print(f"Uppercase:  {result_upper}")

    result_title = manipulator.title(sample_text)
    print(f"Title Case : {result_title}")