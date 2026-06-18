import re

def extract_words(text):
    """
    Extracts all words (sequences of alphanumeric characters) from a multi-line input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        list[str]: A list of extracted words in the order they appear.
    """
    # Use regular expression to find sequences of alphanumeric characters
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_input = '''Hello World! This is a test string with numbers 123 and symbols @#.
Another line here, case sensitive ABC.
Final words: python programming is fun.'''
    
    result = extract_words(sample_input)
    print(result)