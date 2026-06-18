class StringCaseManipulator:
    """A class to efficiently manipulate string cases."""

    def to_lower(self, text: str) -> str:
        """Converts a string to lowercase."""
        return text.lower()

    def to_upper(self, text: str) -> str:
        """Converts a string to uppercase."""
        return text.upper()

    def to_title(self, text: str) -> str:
        """Converts the first character of each word to uppercase and the rest to lowercase."""
        # Using title() handles multiple spaces correctly by treating consecutive whitespace as one separator
        return text.title()

if __name__ == '__main__':
    sample_text = "hello world this is a test string"

    manipulator = StringCaseManipulator()

    print("Original:", repr(sample_text))
    print("Lowercase: ", repr(manipulator.to_lower(sample_text)))
    print("Uppercase: ", repr(manipulator.to_upper(sample_text)))
    print("Title Case: ", repr(manipulator.to_title(sample_text)))