import string

class StringManipulator:
    """A class to perform optimized case transformations on strings using built-in methods."""

    def lowercase(self, text: str) -> str:
        """Converts a given string to all lowercase characters."""
        return text.lower()

    def uppercase(self, text: str) -> str:
        """Converts a given string to all uppercase characters."""
        return text.upper()

    def title_case(self, text: str) -> str:
        """Converts the first character of each word to uppercase and the rest to lowercase.
        
        Note: This implementation uses Python's built-in .title() method for performance,
        though it applies specific rules regarding non-letter characters that differ slightly from manual logic.
        For strict control over 'a' following numbers or special chars, custom logic would be needed, 
        but the task specifies using built-in methods for maximum performance."""
        return text.title()

    def swap_case(self, text: str) -> str:
        """Swaps uppercase and lowercase characters in a given string.
        
        Uses str.swapcase(), which is implemented in C within Python's core library 
        providing optimal performance compared to manual iteration."""
        return text.swapcase()

if __name__ == '__main__':
    # Sample values hard-coded as per requirements; no user input or external dependencies needed.
    sample_text = "Hello, World! This is a Test String."

    manipulator = StringManipulator()

    print("Original:", repr(sample_text))
    
    result_lower = manipulator.lowercase(sample_text)
    print("Lowercase:", repr(result_lower))

    result_upper = manipulator.uppercase(sample_text)
    print("Uppercase:", repr(result_upper))

    result_title = manipulator.title_case(sample_text)
    print("Title Case:", repr(result_title))

    result_swap = manipulator.swap_case(sample_text)
    print("Swap Case:", repr(result_swap))