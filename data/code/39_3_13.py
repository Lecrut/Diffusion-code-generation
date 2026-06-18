import re

def extract_words(text: str) -> list:
    """Extracts all words (sequences of alphanumeric characters) from a multi-line string."""
    # Use regular expression to find sequences of alphanumeric characters and underscores
    return [word for word in re.findall(r'[a-zA-Z0-9_]+', text)]

if __name__ == '__main__':
    sample_input = """Hello, world! This is a test.
It contains numbers: 12345 and mixedCaseWord here.
Also some-punctuated-text."""

    result_words = extract_words(sample_input)
    
    print("Extracted words:")
    for word in result_words:
        print(word)