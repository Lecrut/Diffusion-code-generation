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
        # Using capitalize on words is efficient; split and join ensures correct spacing.
        if not text:
            return ""
        
        parts = [part.capitalize() for part in text.split()]
        return " ".join(parts)

    def swap_case(self, text: str) -> str:
        """Swaps the case of each letter (lower to upper and vice versa)."""
        # The built-in swapcase method is implemented efficiently in CPython.
        return text.swapcase()

if __name__ == '__main__':
    sample_string = "Hello, World! This is a SAMPLE String."
    
    manipulator = StringManipulator()

    print("Original:", sample_string)
    print("Lowercase:", manipulator.to_lowercase(sample_string))
    print("Uppercase:", manipulator.to_uppercase(sample_string))
    print("Title Case: ", manipulator.to_title_case(sample_string))
    print("Swap Case:  ", manipulator.swap_case(sample_string))