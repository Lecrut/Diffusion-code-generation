def get_first_letters(text: str) -> list[str]:
    """
    Returns a list containing the first letter of every word in the input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list where each element is the first character of a word found in the text.
                   Words are sequences of alphabetic characters separated by non-alphabetic boundaries or spaces.
    """
    return [word[0] for word in re.findall(r'\b[a-zA-Z]+\b', text)]

import re

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test."
    result = get_first_letters(sample_text)
    print(result)  # Output: ['H', 'W', 'T', 'I', 'A']