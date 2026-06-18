class StringManipulator:
    """A class providing optimized string manipulation methods."""

    def to_lowercase(self, text: str) -> str:
        """Converts a given string to lowercase using built-in method."""
        return text.lower()

    def to_uppercase(self, text: str) -> str:
        """Converts a given string to uppercase using built-in method."""
        return text.upper()

    def to_title_case(self, text: str) -> str:
        """Converts a given string to title case (first letter of each word capitalized)."""
        # Using capitalize and split/join is generally efficient for standard cases.
        # Alternatively, translate can be used but lower().title() is optimized in CPython.
        return text.title()

    def swap_case(self, text: str) -> str:
        """Swaps the case of each character (uppercase becomes lowercase and vice versa)."""
        return text.swapcase()

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    test_string = "Hello, World! This is a Test String."

    manipulator = StringManipulator()

    print("Original:", test_string)
    print("Lowercase: ", manipulator.to_lowercase(test_string))
    print("Uppercase: ", manipulator.to_uppercase(test_string))
    print("Title Case: ", manipulator.to_title_case(test_string))
    print("Swap Case: ", manipulator.swap_case(test_string))