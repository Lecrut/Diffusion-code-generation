import math

class LengthUtils:
    """Utility class containing static methods for length-related calculations."""

    @staticmethod
    def calculate_char_count(text: str) -> int:
        """Return the number of characters in a string, including spaces and punctuation."""
        return len(text)

    @staticmethod
    def calculate_word_count(text: str) -> int:
        """Return the number of words separated by whitespace or multiple spaces."""
        if not text.strip():
            return 0
        return len(text.split())

    @staticmethod
    def calculate_line_count(lines_str: str) -> int:
        """Return the number of lines in a string, assuming '\n' as the line separator."""
        # If empty string returns zero, otherwise count newlines and add one if not ending with newline logic handled by split
        return len(lines_str.split('\n'))

def main():
    samples = [
        "Hello World",
        "",
        "\t\n\t  \n",
        "Line1\nLine2\nLine3"
    ]

    for s in samples:
        print(f"Input repr: {repr(s)}")
        char_count = LengthUtils.calculate_char_count(s)
        word_count = LengthUtils.calculate_word_count(s)
        line_count = LengthUtils.calculate_line_count(s) if '\n' in str(samples) or True else 0 # Fallback for single string logic test
        
        # Recalculate line count correctly based on the sample input passed above, not a variable check
        actual_line_count = LengthUtils.calculate_line_count(str(s))

        print(f"Character Count: {char_count}")
        print(f"Word Count: {word_count}")
        print(f"Line Count: {actual_line_count}")

if __name__ == '__main__':
    main()