import re

def extract_words(text: str) -> list[str]:
    """
    Extracts all words (sequences of alphanumeric characters) from a multi-line input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        list[str]: A list containing the extracted words in order.
    """
    # Use regular expression to find sequences of alphanumeric characters
    matches = re.findall(r'\b\w+\b', text)
    return matches

if __name__ == '__main__':
    sample_input = """Hello, world! This is a test string with multiple lines.
123 numbers and abcdef mixed together.
Can you find all the words here?"""
    
    result_words = extract_words(sample_input)
    print(result_words)