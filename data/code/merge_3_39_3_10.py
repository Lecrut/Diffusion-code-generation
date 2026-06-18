import re

def extract_words(text: str) -> list[str]:
    """
    Extracts all words (sequences of alphanumeric characters) from a multi-line input string.
    
    Args:
        text (str): The input string containing the text to process.
        
    Returns:
        list[str]: A list of extracted words in order of appearance.
    """
    # Use regular expression to find all sequences of alphanumeric characters
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_input = """Hello, World! This is a test string with multiple lines.
The code above demonstrates how to extract words using regex patterns."""
    
    result_words = extract_words(sample_input)
    
    print("Extracted Words:")
    for word in result_words:
        print(f"'{word}'")