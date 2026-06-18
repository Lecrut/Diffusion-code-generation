import string

class StringManipulator:
    """A class providing optimized string manipulation methods using built-in functions."""

    def to_lowercase(self, text: str) -> str:
        """Converts a given string to lowercase."""
        return text.lower()

    def to_uppercase(self, text: str) -> str:
        """Converts a given string to uppercase."""
        return text.upper()

    def to_title_case(self, text: str) -> str:
        """Converts a given string to title case (first letter of each word capitalized)."""
        # Using the built-in .title() method which is implemented in C for performance.
        return text.title()

    def swap_case(self, text: str) -> str:
        """Swaps the case of all characters in a given string."""
        return text.swapcase()

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    sample_text = "Hello World! This is A Sample String."

    manipulator = StringManipulator()

    print("Original:", sample_text)
    print("Lowercase:", manipulator.to_lowercase(sample_text))
    print("Uppercase:", manipulator.to_uppercase(sample_text))
    print("Title Case:", manipulator.to_title_case(sample_text))
    print("Swap Case:", manipulator.swap_case(sample_text))

    # Additional test with special characters and numbers to ensure robustness.
    complex_text = "Python3.8 is awesome, isn't it? 123!"
    print("\nComplex Text Test:")
    print("Original:", complex_text)
    print("Lowercase:", manipulator.to_lowercase(complex_text))
    print("Uppercase:", manipulator.to_uppercase(complex_text))
    print("Title Case:", manipulator.to_title_case(complex_text))
    print("Swap Case:", manipulator.swap_case(complex_text))