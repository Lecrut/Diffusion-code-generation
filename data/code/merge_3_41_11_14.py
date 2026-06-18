import string

class StringManipulator:
    """A class providing optimized built-in methods for case conversion."""

    def to_lowercase(self, text: str) -> str:
        """Converts a given string to lowercase using the built-in method."""
        return text.lower()

    def to_uppercase(self, text: str) -> str:
        """Converts a given string to uppercase using the built-in method."""
        return text.upper()

    def to_title_case(self, text: str) -> str:
        """Converts a given string to title case (first letter of each word capitalized)."""
        # Using capitalize and split/join is less efficient than str.title for large strings.
        # However, Python's built-in .title() method is implemented in C and highly optimized.
        return text.title()

    def swap_case(self, text: str) -> str:
        """Swaps the case of each character (upper becomes lower, vice versa)."""
        return text.swapcase()

if __name__ == '__main__':
    sample_string = "Hello World! This is a Sample String."

    manipulator = StringManipulator()

    print("Original:", sample_string)
    print("Lowercase: ", manipulator.to_lowercase(sample_string))
    print("Uppercase: ", manipulator.to_uppercase(sample_string))
    print("Title Case: ", manipulator.to_title_case(sample_string))
    print("Swap Case: ", manipulator.swap_case(sample_string))