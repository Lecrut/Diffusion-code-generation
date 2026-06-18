import re

def extract_words(text: str) -> list[str]:
    """Extracts all words (sequences of alphanumeric characters) from input text."""
    # Use regex to find sequences of alphanumeric characters and underscores
    return re.findall(r'\w+', text.lower())

if __name__ == '__main__':
    sample_input = "Hello, World! This is a test string with numbers 12345."
    
    words = extract_words(sample_input)
    
    print("Extracted words:")
    for word in words:
        print(word)