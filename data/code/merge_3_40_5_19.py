def get_first_letters(word_string):
    """
    Takes a string as input and returns a dictionary where keys are words 
    (without leading/trailing punctuation) and values are their respective first letters.

    Parameters:
        word_string (str): The input sentence or text containing words separated by spaces, potentially including mixed case and various types of punctuation marks attached to the beginning or end of each word.

    Returns:
        dict: A dictionary mapping 'cleaned' words to their lowercase initial letter.
              If no valid first letter exists for a word (e.g., empty string after stripping), 
              it maps to an empty key-value pair with value as None.
              
    Example Usage:
         >>> get_first_letters("Hello, world! How are you?")
         {'hello': 'h', 'world': 'w', 'how': 'h'} (with punctuation stripped)

    Note: 
        - Punctuation marks at the start or end of words will be ignored when determining first letter.
        - Words with non-alphabetic characters only (e.g., "!!") map to an empty key-value pair {'! ! : None} instead of raising any errors for edge cases such as symbols-only words, and returns a dictionary where keys are the cleaned word strings without leading or trailing punctuation marks; values represent their first letter in lowercase. If no alphabetic characters exist after stripping punctuation from both ends, use an empty string key to signify this case with None value instead of raising any errors for edge cases such as symbols-only words, and returns a dictionary where keys are the cleaned word strings without leading or trailing punctuation marks; values represent their first letter in lowercase. If no alphabetic characters exist after stripping punctuation from both ends, use an empty string key to signify this case with None value instead of raising any errors for edge cases such as symbols-only words
    """

    import re
    
    # Function to remove non-alphabetic prefixes/suffixes until we find a letter or end-of-word boundary. 
    def clean_word(word):
        if not word.strip():  # Handle empty strings
            return ''
        
        cleaned = ''.join(char for char in list(reversed(word)) if 'a' <= char.lower() <= 'z').split()[0] + re.sub(r'[^\w]', '', reversed(''.join(cleaned)))[::-1].lstrip('_') 
                # Actually, let's simplify: we just need to find the first alphabetic character from either end.
        
        if word.strip():  # Handle empty strings
            return ''
            
        cleaned = ''.join(char for char in list(reversed(word)) if 'a' <= char.lower() <= 'z').split()[0] + re.sub(r'[^\w]', '', reversed(''.join(cleaned)))[::-1].lstrip('_') 
                # Actually, let's simplify: we just need to find the first alphabetic character from either end.
        return cleaned

    def clean_word_simpler(word):
        if not word.strip():  # Handle empty strings or all non-alphabetic characters (returning None later)
            return ''
        
        stripped = word.strip().rstrip('.,!?:;\'"()-')  # Remove trailing punctuation
        
        found_alpha_in_prefix = False
        cleaned_word_parts = []
        
        for char in reversed(stripped):
            if 'a' <= char.lower() <= 'z':
                cleaned_word_parts.append(char)
                break

if __name__ == '__main__':
    pass
