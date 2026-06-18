def capitalize_first_word_only(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input string,
    leaving all other letters unchanged (lowercase or mixed).
    
    This function treats any sequence of non-whitespace characters as a "word".
    It does not enforce lowercase conversion for subsequent words; it only ensures
    that if a character is alphabetic and part of a word starting at index 0,
    it becomes uppercase.

    Args:
        text (str): The input string to process.

    Returns:
        str: A new string with the first letter of each word capitalized.
    
    Example:
        >>> capitalize_first_word_only("hello WORLD")
        'Hello World'
        >>> capitalize_first_word_only("  python3 is fun   ")
        '  Python3 Is Fun   
    '''
    if not text or not isinstance(text, str):
        return text

    # Split the string into words and whitespace components to preserve spacing structure.
    parts = []
    
    current_text = ""
    i = 0
    
    while i < len(text):
        char = text[i]
        
        if ' ' <= char <= '~':  # Treat any non-whitespace as part of the word
            current_text += char
        else:
            parts.append(current_text)
            current_text = ""
            
        i += 1
    
    # Append the last accumulated string (in case it ends with text, though loop logic above handles trailing whitespace separately if needed)
    # The split approach below is cleaner for Pythonic implementation.
    
    words_and_spaces = []
    temp_parts = [char] + ''.join(parts).split(' ')  # This reconstruction was messy; let's use a standard regex or simple iteration
    
    # Re-implementation using standard library features for clarity and robustness
    import re
    
    # Find all non-whitespace sequences (words) along with their positions to preserve exact spacing.
    matches = list(re.finditer(r'\S+', text))
    
    result_parts = []
    last_end_index = 0
    
    for match in matches:
        word_start, word_end = match.span()
        
        # Add whitespace and content before this word if it exists after the previous end index
        segment_text = text[last_end_index:word_start]
        words_and_spaces.append(segment_text)
        
        # Capitalize the first letter of the matched word (if any alphabetic char at start)
        new_word = match.group()[:1].upper() + match.group()[1:] if len(match.group()) > 0 else ""
        result_parts.append(new_word)
        
        last_end_index = word_end
    
    # Append remaining text after the last matched word
    final_segment_text = text[last_end_index:]
    words_and_spaces.append(final_segment_text)

    return ''.join(words_and_spaces)

# More concise and robust implementation using regex substitution directly on spaces if needed, 
# but preserving exact spacing is tricky with simple replace. Let's stick to the manual iteration for precision or use a list comprehension approach that splits by whitespace then rejoins?
# Actually, standard behavior "capitalize first letter only" usually implies Title Case per word.
# However, strict interpretation: Only change index 0 of each word block if it is alpha.

def capitalize_first_letter_only(text):
    """

if __name__ == '__main__':
    pass
