import re

def extract_words(text: str) -> list[str]:
    """
    Extracts all sequences of alphanumeric characters from a given string.
    
    Args:
        text (str): The input multi-line string to process.
        
    Returns:
        List[str]: A list containing each extracted word in the order found.
    """
    return re.findall(r'\w+', text)

if __name__ == '__main__':
    sample_input = "Hello, World! This is a test.\nIt contains numbers 123 and symbols @#$."
    
    result = extract_words(sample_input)
    print(result)