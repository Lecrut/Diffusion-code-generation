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
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        # Using built-in capitalize and split/join logic is less efficient than direct translation for complex cases,
        # but Python's .title() handles most standard title casing requirements efficiently.
        return text.title()

    def swap_case(self, text: str) -> str:
        """Swaps the case of each character in the string."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        # Built-in swapcase is implemented in C and offers maximum performance.
        return text.swapcase()

if __name__ == '__main__':
    sample_string = "Hello World! This Is A Test String."

    manipulator = StringManipulator()

    print("Original:", sample_string)
    print("Lowercase: ", manipulator.to_lowercase(sample_string))
    print("Uppercase: ", manipulator.to_uppercase(sample_string))
    print("Title Case: ", manipulator.to_title_case(sample_string))
    print("Swap Case: ", manipulator.swap_case(sample_string))