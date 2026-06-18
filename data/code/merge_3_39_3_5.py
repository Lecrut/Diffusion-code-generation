import re

def extract_words(text: str) -> list[str]:
    """
    Extracts all words (sequences of alphanumeric characters) from the input text.
    
    Args:
        text (str): The multi-line string to process.
        
    Returns:
        list[str]: A list containing each extracted word as a separate element.
    """
    return re.findall(r'\w+', text.lower())

if __name__ == '__main__':
    sample_input = '''Hello, World! This is a test script for Python regex.
It handles multiple lines and special characters gracefully.'''

    result_list = extract_words(sample_input)
    
    print(f"Input:\n{sample_input}\n")
    print("Extracted words:")
    print(result_list)