import sys

def get_first_letters(text: str) -> list[str]:
    """
    Extracts the first letter of every word from the input text.
    
    Args:
        text (str): The input string containing words separated by whitespace or newlines.
        
    Returns:
        List[str]: A list of single-character strings representing the first letter 
                   of each alphabetic character found at the start of a 'word'.
                   
       Note: This implementation considers any sequence of non-alphabetic characters as a separator,
       but only returns letters that are part of an actual word (alphabetic). If a string starts with a number or symbol
       without following it by a letter immediately in some definitions, this logic treats the first alphabetic 
       character encountered after whitespace/symbols as the start. However, to strictly follow "first letter of every word",
       we define a 'word' here as any contiguous sequence of alphanumeric characters (including hyphens and underscores).
       
    """
    
    words = text.split()
    result_chars = []
    
    for word in words:
        if not word:
            continue
            
        # Check the first character to see if it is a letter
        first_char = word[0]
        
        if 'a' <= first_char <= 'z':
            result_chars.append(first_char)
        elif 'A' <= first_char <= 'Z':
            result_chars.append(first_char)
            
    return result_chars

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of running without user input.
    sample_input = """Hello world!
Python is great.
Multi-line test."""

    output_lines = get_first_letters(sample_input)
    
    for char in output_lines:
        print(char, end='')