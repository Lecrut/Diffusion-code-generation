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
        # Using capitalize and split/join logic is often slower than just calling .title(),
        # but Python's built-in .title() handles contractions like "don't" correctly.
        return text.title()

    def swap_case(self, text: str) -> str:
        """Swaps the case of each character in the string using a generator expression."""
        return ''.join(char.swapcase() for char in text)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    test_string = "Hello, World! This is an EXAMPLE."

    manipulator = StringManipulator()

    print("Original:", test_string)
    print("Lowercase: ", manipulator.to_lowercase(test_string))
    print("Uppercase: ", manipulator.to_uppercase(test_string))
    print("Title Case: ", manipulator.to_title_case(test_string))
    print("Swap Case: ", manipulator.swap_case(test_string))