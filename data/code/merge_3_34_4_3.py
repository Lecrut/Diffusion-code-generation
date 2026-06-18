import sys

def capitalize_first_letter(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input text.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first character of each word capitalized.
             Non-alphabetic characters are left unchanged if they precede a capitalization,
             but standard title casing is applied where alphabetic sequences exist.
    
    Note: This implementation uses Python's built-in split() and join() methods 
         to handle multiple spaces correctly by treating consecutive whitespace as a single separator.
    """
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    
    samples = [
        "hello world",
        "python is awesome",
        "this   has   multiple   spaces",
        "mixed CASE 123 and symbols!",
    ]

    for sample in samples:
        result = capitalize_first_letter(sample)
        print(f"Input: '{sample}'")
        print(f"Output: '{result}'\n")