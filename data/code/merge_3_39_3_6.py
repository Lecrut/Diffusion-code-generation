import re

def extract_words(text: str) -> list[str]:
    """
    Extracts all words (sequences of alphanumeric characters) from a multi-line input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        list[str]: A list containing each extracted word in order.
    """
    # Use regular expression to find sequences of alphanumeric characters and underscores
    words = re.findall(r'\b\w+\b', text)
    return words

if __name__ == '__main__':
    sample_input = "Hello, world! This is a test.\nIt contains multiple lines with numbers 12345."
    
    result_words = extract_words(sample_input)
    
    print("Extracted words:")
    for word in result_words:
        print(word)