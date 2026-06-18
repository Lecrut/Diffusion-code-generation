class StringManipulator:
    """A class providing optimized string manipulation methods using built-in functions."""

    def to_lowercase(self, text: str) -> str:
        """Converts a given string to lowercase."""
        return text.lower()

    def to_uppercase(self, text: str) -> str:
        """Converts a given string to uppercase."""
        return text.upper()

    def to_title_case(self, text: str) -> str:
        """Converts the first character of each word in the string to upper case."""
        return text.title()

    def swap_case(self, text: str) -> str:
        """Swaps the case for all characters in a given string. Upper becomes lower and vice versa."""
        return text.swapcase()

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_string = "Hello, World! This is an EXAMPLE."

    manipulator = StringManipulator()

    print("Original:", test_string)
    print("Lowercase: ", manipulator.to_lowercase(test_string))
    print("Uppercase: ", manipulator.to_uppercase(test_string))
    print("Title Case: ", manipulator.to_title_case(test_string))
    print("Swap Case: ", manipulator.swap_case(test_string))