class StringCaseManipulator:
    """A class to efficiently manipulate string cases."""

    def __init__(self, text: str):
        """Initialize with a string."""
        self.text = text
    
    @staticmethod
    def to_lower(text: str) -> str:
        """Convert all characters in the string to lowercase."""
        return text.lower()

    @staticmethod
    def to_upper(text: str) -> str:
        """Convert all characters in the string to uppercase."""
        return text.upper()

    @classmethod
    def title(cls, text: str) -> str:
        """Title case conversion (first character of each word capitalized)."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        
        # Split into words, capitalize first letter of each, join back
        return " ".join(word.capitalize() for word in text.split())

    def to_lower(self) -> str:
        """Return the input string converted to lowercase."""
        return self.to_lower(self.text)

    def to_upper(self) -> str:
        """Return the input string converted to uppercase."""
        return self.to_upper(self.text)

    @classmethod
    def title(cls, text: str):
        """Title case conversion (first character of each word capitalized)."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        
        # Split into words, capitalize first letter of each, join back
        return " ".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    sample_text = "Hello World Python Programming"

    print(f"Original: {sample_text}")
    
    manipulator = StringCaseManipulator(sample_text)

    lower_result = manipulator.to_lower()
    upper_result = manipulator.to_upper()
    title_result = cls.title(sample_text)  # Using class method directly or instance wrapper if desired
    
    print(f"Lowercase: {lower_result}")
    print(f"Uppercase: {upper_result}")
    print(f"Title Case: {title_result}")

    # Demonstrate static methods on raw string as well for clarity
    lower_static = StringCaseManipulator.to_lower(sample_text)
    upper_static = StringCaseManipulator.to_upper(sample_text)

    assert lower_result == "hello world python programming", "Lowercase mismatch"
    assert upper_result == "HELLO WORLD PYTHON PROGRAMMING", "Uppercase mismatch"
    assert title_result == "Hello World Python Programming", "Title case mismatch"
    
    print("All tests passed.")