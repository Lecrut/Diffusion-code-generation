import re

def extract_words(text: str) -> list[str]:
    """
    Extracts all sequences of alphanumeric characters from the input text.
    
    Args:
        text (str): The multi-line string to process.
        
    Returns:
        list[str]: A list containing each extracted word in order.
    """
    # Use a regular expression to find all contiguous alphanumeric sequences.
    return re.findall(r'\w+', text)

if __name__ == '__main__':
    sample_input = "Hello world! This is a multi-line example.\nIt contains numbers 123 and symbols @#$."
    
    result_words = extract_words(sample_input)
    
    print("Extracted words:", result_words)