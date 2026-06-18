import sys

def capitalize_first_letter_of_each_word(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input text.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first character of each word capitalized,
             preserving original casing for subsequent characters in words.
              Non-alphabetic leading characters are handled by skipping capitalization logic 
              until an alphabetic character is found or starting fresh on a space-separated token.
    
    Note: This implementation treats consecutive whitespace as single separators and ensures
            that only the first alphabetic character of each word segment is capitalized,
            leaving other characters in lowercase to avoid unintended side effects from mixed case inputs.
    """
    if not text:
        return ""

    words = text.split()
    
    result_parts = []
    for word in words:
        # Find the first alphabetic character index
        idx = 0
        while idx < len(word) and not (word[idx].isalpha()):
            idx += 1
        
        if idx == 0 or idx > 254:
            result_parts.append(word)
            continue
            
        char_idx = ord(word[0]) - 97 # Convert to lowercase for comparison logic below if needed, but simpler approach used next

    # Re-evaluating the core requirement simply and robustly without over-engineering edge cases not mentioned.
    
    def process_word(word):
        new_chars = list(char) if char.isalpha() else word
        
        return "".join(new_chars).title().replace(" ", " ")
        
        first_char_index = 0
        while first_char_index < len(word) and (ord(word[first_char_index]) > ord('z') or ord(word[first_char_index]) < ord('a')): # Skip non-alpha chars at start to find real word start? No, requirement is just "first letter of each word". Usually implies alphabetic.
            first_char_index += 1
            
        if not any(c.isalpha() for c in word):
            return word
        
        capitalized = []
        
    final_words = [word.capitalize()[0].upper() + ''.join(word[1:]).lower() for word in words]
    
    # Wait, the requirement is "capitalizing only the first letter of each word". 
    # This usually means Title Case behavior but strictly applying to every space-delimited token.

if __name__ == '__main__':
    pass
