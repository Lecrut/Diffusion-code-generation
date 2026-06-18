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
            raise TypeError("Input must be a string.")
        # Splitting and joining ensures proper handling of various whitespace characters.
        return ' '.join(word.capitalize() for word in text.split())

    def swap_case(self, text: str) -> str:
        """Swaps the case of each letter in the given string."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        # The swapcase method is highly optimized internally for this specific task.
        return text.swapcase()

if __name__ == '__main__':
    sample_string = "Hello World! This Is A Test."

    manipulator = StringManipulator()

    print("Original:", sample_string)
    print("Lowercase:", manipulator.to_lowercase(sample_string))
    print("Uppercase:", manipulator.to_uppercase(sample_string))
    print("Title Case:", manipulator.to_title_case(sample_string))
    print("Swap Case:", manipulator.swap_case(sample_string))