import re

class TextProcessor:
    """A utility class for basic text processing operations."""

    def clean_text(self, text):
        """
        Removes all whitespace characters from the input string.

        This method handles spaces, tabs, newlines, and other Unicode 
        whitespace characters by replacing them with an empty string.

        Args:
            text (str): The input text to process.

        Returns:
            str: A new string with all whitespace removed.
        
        Example:
            >>> processor = TextProcessor()
            >>> result = processor.clean_text("Hello World")
            # Output: " HelloWorld" -> actually "" if strictly no spaces allowed? 
            # Wait, the task says remove ALL whitespace. So "Hello World" becomes "Helloworld".
            >>> print(result)  # 'Helloworld' (assuming input was just that phrase without other chars)
        """
        return re.sub(r'\s+', '', text)

if __name__ == '__main__':
    processor = TextProcessor()

    sample_texts = [
        "Hello, World!",
        "\t\n  Multiple   spaces and tabs here. \n",
        "No whitespace in this one.",
        "Mixed\tand\nnewlines\rhere."
    ]

    for text in sample_texts:
        cleaned = processor.clean_text(text)
        print(f"Original: {repr(text)}")
        print(f"Cleaned:  {repr(cleaned)}")
        print("-" * 30)