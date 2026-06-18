import re

def extract_words(text):
    """
    Extracts all words (sequences of alphanumeric characters) from a multi-line input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        list[str]: A list of extracted words in the order they appear.
    """
    # Use regex to find all sequences of alphanumeric characters
    return re.findall(r'\w+', text)

if __name__ == '__main__':
    sample_input = "Hello, World! This is a test.\nIt contains multiple lines and punctuation."
    
    words = extract_words(sample_input)
    
    print("Extracted words:")
    for word in words:
        print(word)