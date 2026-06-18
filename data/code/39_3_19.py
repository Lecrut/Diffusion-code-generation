import re

def extract_words(text: str) -> list[str]:
    """
    Extracts all words (sequences of alphanumeric characters) from a multi-line input string.
    
    Args:
        text (str): The input string to process, potentially containing multiple lines and punctuation.
        
    Returns:
        list[str]: A list of extracted words in the order they appear.
    """
    # Use regular expression to find sequences of alphanumeric characters
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_input = "Hello, world! This is a multi-line example.\nIt contains numbers: 123 and symbols @#$."
    
    words_list = extract_words(sample_input)
    
    print("Extracted words:")
    for word in words_list:
        print(word.lower())