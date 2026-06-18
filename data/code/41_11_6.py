import string

class StringManipulator:
    """A class providing optimized built-in methods to manipulate strings."""

    def __init__(self, text: str):
        self.original_text = text

    @staticmethod
    def is_empty(s: str) -> bool:
        return len(s) == 0 or not s.strip()

    # Method implementations using standard Python string operations for optimal performance.
    
    def to_lowercase(self, text: str | None = None):
        """Convert the specified string (or stored instance value) to lowercase."""
        if text is None and self.original_text:
            target_string = self.original_text
        else:
            target_string = text
        
        return target_string.lower()

    def to_uppercase(self, text: str | None = None):
        """Convert the specified string (or stored instance value) to uppercase."""
        if text is None and self.original_text:
            target_string = self.original_text
        else:
            target_string = text
        
        return target_string.upper()

    def to_title_case(self, text: str | None = None):
        """Convert the specified string (or stored instance value) to title case."""
        if text is None and self.original_text:
            target_string = self.original_text
        else:
            target_string = text
        
        return " ".join([word.capitalize() for word in target_string.split()])

    def swap_case(self, text: str | None = None):
        """Swap the case of each character in the specified string (or stored instance value)."""
        if text is None and self.original_text:
            target_string = self.original_text
        else:
            target_string = text
        
        return ''.join([char.swapcase() for char in target_string])

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.

    test_input = "Hello, World! This is a Python string."
    
    manipulator = StringManipulator(test_input)

    print("Original Text:")