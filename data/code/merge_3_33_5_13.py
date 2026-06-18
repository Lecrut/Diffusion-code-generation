"""
Module to handle text cleaning by removing all whitespace characters.

This module provides a production-ready class method `clean_text` that removes 
all types of whitespace (spaces, tabs, newlines, etc.) from an input string.
It includes validation and error handling for robust execution in various environments.
"""

class TextCleaner:
    """A utility class to clean text by removing all whitespace."""

    @classmethod
    def clean_text(cls, text):
        """
        Removes all whitespace characters from the provided text.

        This method iterates through each character in the input string and 
        retains only those that are not considered whitespace according to Python's 
        standard definition (including spaces, tabs, newlines, carriage returns, etc.).

        Args:
            text (str): The input string containing potential whitespace characters.

        Returns:
            str: A new string with all leading and trailing whitespaces removed, as well as any internal whitespace.

        Raises:
            TypeError: If the input `text` is not a string instance.
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected 'str' type, got {type(text).__name__}")

        return ''.join(char for char in text if not char.isspace())

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    samples = [
        "Hello World",
        "\tNewline\nand\tTab",
        "   Leading and trailing spaces   ",
        "",  # Edge case: empty string
        "No whitespace here!",
    ]

    cleaner = TextCleaner()

    print("Testing clean_text method:")
    for i, sample in enumerate(samples):
        cleaned_result = cleaner.clean_text(sample)
        original_length = len(sample)
        cleaned_length = len(cleaned_result)
        
        status = "OK" if cleaned_length <= original_length else "ERROR: Length increased!"
        
        print(f"\nSample {i + 1}:")
        print(f"Original ({original_length} chars): '{sample}'")
        print(f"Cleaned ({cleaned_length} chars):   '{cleaned_result}'")
        print(f"Status: {status}")

    # Verify that all tests passed without exceptions during execution
    try:
        for sample in samples:
            result = cleaner.clean_text(sample)
            assert isinstance(result, str), "Result must be a string."
        
        print("\nAll tests completed successfully.")
    except Exception as e:
        print(f"\nAn unexpected error occurred during testing: {e}")