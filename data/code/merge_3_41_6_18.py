class StringCaseManipulator:
    """A class to efficiently manipulate string cases."""

    def to_lower(self, text: str) -> str:
        """Converts a string to lowercase."""
        return text.lower()

    def to_upper(self, text: str) -> str:
        """Converts a string to uppercase."""
        return text.upper()

    def to_title(self, text: str) -> str:
        """Converts a string to title case (first letter of each word capitalized)."""
        return text.title()

if __name__ == '__main__':
    sample_text = "hello world this is a test"
    
    manipulator = StringCaseManipulator()

    result_lower = manipulator.to_lower(sample_text)
    print(f"Lowercase: '{result_lower}'")

    result_upper = manipulator.to_upper(sample_text)
    print(f"Uppercase: '{result_upper}'")

    result_title = manipulator.to_title(sample_text)
    print(f"Title Case: '{result_title}'")