import re

def extract_words(text: str) -> list[str]:
    """
    Extracts all words (sequences of alphanumeric characters) from a multi-line input string.

    Args:
        text (str): The input string to process, which may contain multiple lines and various separators.

    Returns:
        list[str]: A list containing the extracted words in order.
    """
    # Use regular expression to find all sequences of alphanumeric characters
    found_words = re.findall(r'\b\w+\b', text)
    return found_words

if __name__ == '__main__':
    sample_input = "Hello, World! This is a test.\n\nAnother line with numbers: 123 and symbols @#$."

    words = extract_words(sample_input)
    print(words)