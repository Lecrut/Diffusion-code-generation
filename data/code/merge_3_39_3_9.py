import re

def extract_words(text: str) -> list[str]:
    """
    Extracts all sequences of alphanumeric characters from the input string.
    
    Args:
        text (str): The multi-line input string to process.
        
    Returns:
        list[str]: A list containing each extracted word in order.
    """
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_input = '''Python is great! 
It has many libraries for data science. 
We can analyze big datasets easily.'''

    words_list = extract_words(sample_input)
    
    # Print the result to verify execution without user interaction
    print(words_list)