def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input string,
    preserving the case of all other characters.

    Args:
        text (str): The input string to process.

    Returns:
        str: A new string with only the first letter of each word capitalized.
    """
    if not text or not isinstance(text, str):
        return text
    
    result = []
    
    # Split into words while preserving whitespace structure for non-word characters
    parts = text.split()
    
    for part in parts:
        if len(part) == 0:
            continue
            
        word_chars = list(part)
        
        # Capitalize the first letter of each alphabetic character sequence (word)
        i = 0
        while i < len(word_chars):
            char_code = ord(word_chars[i])
            
            if ('A' <= char_code <= 'Z') or ('a' <= char_code <= 'z'):
                # Check if it's the start of a word (uppercase after space, uppercase itself)
                is_start_of_word = False
                
                # If first character and already uppercase -> keep as is? 
                # Actually task says "capitalize", implying ensure capital.
                # But example usually implies: hello world -> Hello World
                if char_code >= 'a' and char_code <= 'z':
                    word_chars[i] = chr(ord(word_chars[i]) - 32)  # Convert to upper
                
                i += 1
            
            elif char_code == ord(' ') or (char_code < ord('A') and char_code > ord('Z')):
                is_start_of_word = True
        
        result.append("".join(word_chars))
    
    return " ".join(result)

def better_capitalize(text: str) -> str:
    """
    Robust implementation using regex to find word boundaries.
    Replaces the first character of each alphabetic sequence with its uppercase version,
    leaving everything else unchanged.
    
    Args:
        text (str): The input string.

    Returns:
        str: Processed string.
    """
    import re
    
    # Find all sequences of letters/numbers/digits that count as "words" or tokens for capitalization logic?
    # Actually, simpler approach per task requirements ("first letter of each word"):
    # We can iterate through the string and track if we are at the start of a new lexical token.
    
    words = text.split()
    output_words = []
    
    for w in words:
        if not w: continue
        
        # Capitalize strictly the first letter found (assuming standard definition)
        # If input is "hello world", result should be "Hello World"
        
        # Convert to list of chars
        char_list = list(w.lower()) 
        # But task says preserve rest casing. So we must check original case logic carefully?
        # Re-reading: "capitalizes only the first letter... preserving the rest".
        # This usually means if input is "hElLo", output should be "HEllo"? Or "HelLo"? 
        # Standard interpretation for this phrasing in coding tests (like LeetCode):
        # Input: "Hello World" -> Output: "Hello World"
        # Input: "hello world" -> Output: "Hello World"
        
        # Let's implement standard title case but only touching the first letter per word.
        if len(w) == 0: continue
        
        capitalized_w = w[0].upper() + w[1:]
        output_words.append(capitalized_w)
    
    return ' '.join(output_words)

# Alternative robust version handling non-standard words like hyphenated or multiple dots?

if __name__ == '__main__':
    pass
