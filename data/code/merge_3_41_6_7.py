class StringCaseManipulator:
    """A class to efficiently manipulate string case formats."""

    @staticmethod
    def to_lower(s: str) -> str:
        """Convert a string to all lowercase letters."""
        return s.lower()

    @staticmethod
    def to_upper(s: str) -> str:
        """Convert a string to all uppercase letters."""
        return s.upper()

    @staticmethod
    def to_title(s: str) -> str:
        """Convert the first character of each word to uppercase and the rest to lowercase."""
        # Python's built-in title method handles this efficiently, 
        # but we ensure it respects standard casing rules without external dependencies.
        return s.title()

if __name__ == '__main__':
    sample_string = "hElLo WoRLd PyThOn"
    
    print(f"Original: {sample_string}")
    print(f"Lowercase: {StringCaseManipulator.to_lower(sample_string)}")
    print(f"Uppercase: {StringCaseManipulator.to_upper(sample_string)}")
    print(f"Title Case: {StringCaseManipulator.to_title(sample_string)}")