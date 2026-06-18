def capitalize_words(input_string):
    """
    Capitalizes the first letter of each word while preserving the casing 
    of the remaining letters in that word.
    
    Args:
        input_string (str): The string to process
        
    Returns:
        str: A new string with the first character capitalized for each word
        
    Note: This implementation handles punctuation as part of words, so it only 
           capitalizes alphabetic characters at the start of a sequence that begins after whitespace.
    """
    result = []
    
    # Split into tokens based on whitespace to handle multiple spaces correctly
    tokens = input_string.split()
    
    for token in tokens:
        if not token:
            continue
            
        capitalized_token = ""
        
        for i, char in enumerate(token):
            # Capitalize only the first alphabetic character of a word
            is_first_letter = (i == 0) or not any(c.isalpha() for c in token[:i])
            
            if char.isalpha():
                if is_first_letter:
                    capitalized_token += char.upper()

if __name__ == '__main__':
    pass
