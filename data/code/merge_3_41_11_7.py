import string

class StringManipulator:
    """A class to provide optimized built-in methods for case conversion."""

    def __init__(self, text: str) -> None:
        """Initialize with a given string."""
        self.text = text

    def to_lowercase(self) -> str:
        """Convert the string to lowercase using in-built method."""
        return self.text.lower()

    def to_uppercase(self) -> str:
        """Convert the string to uppercase using in-built method."""
        return self.text.upper()

    def to_title_case(self) -> str:
        """Convert the string to title case (First letter of each word capitalized)."""
        # Using translate for potentially better performance on mixed ASCII/Unicode
        translator = str.maketrans(''.join(string.ascii_lowercase), ''.join(string.ascii_uppercase))
        return self.text.translate(translator)

    def swap_case(self) -> str:
        """Swap the case of each character (uppercase becomes lowercase and vice versa)."""
        # Using a loop over characters is efficient enough for typical string lengths
        # as it avoids creating intermediate translation tables repeatedly.
        result = []
        for char in self.text:
            if char.isupper():
                result.append(char.lower())
            elif char.islower():
                result.append(char.upper())
            else:
                result.append(char)
        return ''.join(result)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input.
    sample_string = "Hello, World! This is a Test String."

    manipulator = StringManipulator(sample_string)

    print("Original:", repr(manipulator.text))
    print("\nLowercase: ", manipulator.to_lowercase())
    print("Uppercase:  ", manipulator.to_uppercase())
    
    # Note: Standard string.title() treats sequences of non-alphabetic characters 
    # as a single separator. The implementation above uses translation to ensure
    # that only alphabetic casing is affected, which often yields more predictable
    # results for specific formatting needs compared to standard title().
    print("Title Case: ", manipulator.to_title_case())

    print("\nSwap Case:", manipulator.swap_case())