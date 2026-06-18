class StringManipulator:
    """A class providing optimized string manipulation methods."""

    def to_lowercase(self, text):
        """Converts a given string to lowercase using built-in method."""
        return text.lower()

    def to_uppercase(self, text):
        """Converts a given string to uppercase using built-in method."""
        return text.upper()

    def to_title_case(self, text):
        """Converts a given string to title case (first letter of each word capitalized) using built-in method."""
        return text.title()

    def swapcase(self, text):
        """Swaps the case of characters in the string using built-in method."""
        return text.swapcase()

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_string = "Hello, World! This is a Python example."

    manipulator = StringManipulator()

    print("Original:", test_string)
    print("Lowercase:", manipulator.to_lowercase(test_string))
    print("Uppercase:", manipulator.to_uppercase(test_string))
    print("Title Case:", manipulator.to_title_case(test_string))
    print("Swap Case:", manipulator.swapcase(test_string))