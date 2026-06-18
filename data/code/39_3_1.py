import re

def extract_words(text: str) -> list[str]:
    """Extracts all sequences of alphanumeric characters from the input text."""
    # Find all matches using regex pattern that captures alphanumeric strings separated by any non-alphanumeric character or whitespace
    words = re.findall(r'\b\w+\b', text)
    return words

if __name__ == '__main__':
    sample_input = """Hello, world! This is a test script.
Python is great for extracting data from complex strings."""

    result_words = extract_words(sample_input)

    # Print the extracted list of words to verify functionality
    print(result_words)