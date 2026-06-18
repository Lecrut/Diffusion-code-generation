import re

def extract_words(text: str) -> list[str]:
    """
    Extracts all alphanumeric words from a multi-line input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List of strings, each being an extracted word found in the text.
    """
    # Use regex to find sequences of alphanumeric characters and underscores
    return re.findall(r'\w+', text)

if __name__ == '__main__':
    sample_input = "Hello world! This is a test string with numbers 12345.\nIt contains multiple lines too."
    
    result = extract_words(sample_input)
    
    print("Extracted words:")
    for word in result:
        print(word)