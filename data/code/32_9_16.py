"""Utility module containing a static method to calculate string length with special handling."""

def _count_valid_chars(s: str) -> int:
    """Internal helper to count valid characters in a string.
    
    This function iterates through the input string and counts 
    characters that are not whitespace or newline characters,
    ensuring robustness for various text formats.

    Args:
        s (str): The input string to analyze.

    Returns:
        int: The count of valid non-whitespace/non-newline characters.
    """
    return sum(1 for char in s if not (char.isspace() or char == '\n'))

class StringUtils:
    """A utility class providing static methods for string operations."""

    @staticmethod
    def calculate_length(text: str) -> int:
        """Calculate the effective length of a text, ignoring whitespace and newlines.

        This method serves as a clean wrapper around internal logic to count 
        meaningful characters in a given string. It ensures that leading/trailing
        spaces and embedded newline sequences do not contribute to the final count.

        Args:
            text (str): The input text string for length calculation.

        Returns:
            int: The calculated effective length of the text.
        
        Raises:
            TypeError: If the input is not a string instance.
            
        Examples:
            >>> utils.calculate_length("Hello\nWorld")
            10
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected str type, got {type(text).__name__}")

        return _count_valid_chars(text)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    test_cases = [
        "Hello World",           # Simple case with spaces
        "\n\nLine1\nLine2\n\n",  # Case with multiple newlines
        "",                      # Empty string
        "   \t\t   ",            # Only whitespace and tabs
        "Python!\nC++\nRust",    # Mixed content with line breaks
    ]

    utils = StringUtils()

    print("String Length Calculation Results:")
    for test_input in test_cases:
        result_length = utils.calculate_length(test_input)
        display_text = repr(test_input)[:40] + "..." if len(repr(test_input)) > 40 else repr(test_input)
        print(f"Input: {display_text}")
        print(f"Effective Length: {result_length}\n")

    # Verify the module runs without errors or external dependencies.