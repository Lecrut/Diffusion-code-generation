def extract_first_letters(text: str) -> list[str]:
    """
    Extracts a list of strings, where each string is the first letter 
    of a word found in the input text. Words containing only punctuation 
    are ignored and do not produce an output.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list of single-character strings representing 
                   the first letter of each valid word in the order they appear.
    """
    # Split the text into tokens based on any whitespace or non-alphabetic character boundaries.
    # We look for sequences containing at least one alphabetic character to identify words.
    
    result = []
    current_word_chars = []

    for char in text:
        if 'a' <= char.lower() <= 'z':  # Check if the character is an alphabet letter (case-insensitive)
            current_word_chars.append(char)
        else:
            # If we encounter a non-alphabetic character and our current buffer has letters, 
            # it means a word boundary was crossed. We process the collected characters next.
            if len(current_word_chars) > 0:
                result.extend([c.lower() for c in current_word_chars])
                current_word_chars = []

    # Process any remaining characters after the loop finishes (e.g., end of string).
    if len(current_word_chars) > 0:
        result.extend([c.lower() for c in current_word_chars])

    return result

if __name__ == '__main__':
    pass
