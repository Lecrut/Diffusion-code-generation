import re

class TextProcessor:
    """A utility class for processing text data."""

    def clean_text(self, text):
        """
        Removes all whitespace characters from the input string.

        This method handles spaces, tabs, newlines, and other Unicode 
        whitespace characters by replacing them with an empty string.

        Args:
            text (str): The input text to process.

        Returns:
            str: A new string with all whitespace removed.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        
        # Using regex to match any Unicode whitespace character and replace it with empty string
        return re.sub(r'\s+', '', text)

if __name__ == '__main__':
    processor = TextProcessor()

    sample_texts = [
        "Hello, World!",
        "\t\n  Multiple   spaces\tand\nnewlines",
        "No whitespace here",
        "Mixed: \u00a0\u200b\u3000 invisible chars"
    ]

    for text in sample_texts:
        cleaned = processor.clean_text(text)
        print(f"Original: {repr(text)}")
        print(f"Cleaned:  {repr(cleaned)}\n")