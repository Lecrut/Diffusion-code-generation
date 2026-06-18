class StringCaseManipulator:
    """A class to efficiently manipulate string cases."""

    def to_lower(self, s: str) -> str:
        """Converts a string to lowercase."""
        return s.lower()

    def to_upper(self, s: str) -> str:
        """Converts a string to uppercase."""
        return s.upper()

    def to_title(self, s: str) -> str:
        """Converts the first character of each word to uppercase and the rest to lowercase."""
        # Using title() handles multiple spaces correctly by collapsing them as per standard behavior,
        # or keeps leading/trailing whitespace if desired. Standard title() is used for efficiency.
        return s.title()

if __name__ == '__main__':
    sample_text = "Hello World this Is A Test String"

    manipulator = StringCaseManipulator()

    print("Original:", sample_text)
    print("Lowercase: ", manipulator.to_lower(sample_text))
    print("Uppercase: ", manipulator.to_upper(sample_text))
    print("Title Case: ", manipulator.to_title(sample_text))