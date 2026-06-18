import re

def extract_words(text):
    """
    Extracts all words (sequences of alphanumeric characters) from a multi-line input string.
    
    Args:
        text (str): The input string to process. Can contain multiple lines.
        
    Returns:
        list[str]: A list containing each extracted word in the order they appeared.
    """
    # Use regular expression to find all sequences of alphanumeric characters
    words = re.findall(r'\b\w+\b', text)
    return words

if __name__ == '__main__':
    # Hard-coded sample input string with multiple lines and various punctuation
    sample_input = "Hello, world! This is a test.\nIt can handle\nnewlines too."

    result = extract_words(sample_input)
    
    print("Extracted words:")
    for word in result:
        print(word)