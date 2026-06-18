import re

class TextProcessor:
    """A utility class for performing basic text cleaning operations."""

    def clean_text(self, text):
        """
        Removes all whitespace characters from the input string.

        This method handles spaces, tabs, newlines, and other Unicode 
        whitespace characters by replacing them with an empty string.

        Args:
            text (str): The input string to be cleaned of whitespace.

        Returns:
            str: A new string with all whitespace removed.
        
        Example:
            >>> processor = TextProcessor()
            >>> result = processor.clean_text("Hello World")
            >>> print(result)
            HelloWorld
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected string input, got {type(text).__name__}")

        # Using regex to match any Unicode whitespace character and replace with empty string
        return re.sub(r'\s+', '', text)

if __name__ == '__main__':
    processor = TextProcessor()

    sample_texts = [
        "Hello World",
        "\tNewlines\nand\ttabs",
        "  Multiple   spaces  ",
        "No whitespace here",
        "Mixed: \n tab \r space"
    ]

    for text in sample_texts:
        cleaned_text = processor.clean_text(text)
        print(f"Original: {repr(text)}")
        print(f"Cleaned:  {repr(cleaned_text)}")
        print("-" * 20)