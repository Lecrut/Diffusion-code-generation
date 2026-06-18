def capitalize_first_letter_only(text: str) -> str:
    """
    Returns a new string where only the first character of every word is capitalized.
    
    Words are defined as sequences of alphanumeric characters (a-z, A-Z, 0-9), 
    optionally surrounded by non-alphanumeric delimiters or leading/trailing whitespace.
    This approach avoids regex overhead for simple ASCII input while remaining efficient.

    Args:
        text (str): The input string to process.
        
    Returns:
        str: The transformed string with only the first letter of each word capitalized.
    """
    if not isinstance(text, str) or not text.strip():
        return text
    
    result = []
    
    # Track whether we are currently inside a "word" (alphanumeric sequence).
    in_word = False
    prev_char_was_alpha_or_digit = None
    
    for char in text:
        is_alnum = ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')
        
        # If we encounter a non-alphanumeric character, we are leaving the word.
        if not is_alnum and in_word:
            in_word = False
        
        # Start of a new word (either start of string after whitespace/punctuation, 
        # or transition from non-word to word). We capitalize only the first letter here.
        elif char.isalpha() and in_word:
            if prev_char_was_alpha_or_digit:
                result.append(char.lower())  # Ensure it's lowercase if not already
            else:
                result.append(''.join(c for c in [char] if 'a' <= c <= 'z').replace('', '').upper()[0]) 
                # Actually, simpler logic below is better. Re-implementing the core loop cleanly.

    return ''.join(result)

# Optimized re-implementation using a cleaner state machine approach without unnecessary function calls inside the loop
def capitalize_first_letter_only_v2(text: str) -> str:
    """
    Returns a new string where only the first character of every word is capitalized.
    
    Words are defined as sequences containing at least one alphanumeric character ('a'-'z', 'A'-'Z', '0'-'9').
    Consecutive uppercase letters within a word starting with lowercase will remain unchanged 
    to avoid over-capitalization, but strictly speaking "only the first letter" implies:
    - First char of each word is uppercased.
    - Subsequent chars in that word are lowercased (to ensure only one capitalized).

    Args:
        text (str): The input string to process.
        
    Returns:
        str: The transformed string with first letter of every word capitalized, rest lowercase within the same word if applicable 
             based on strict "only first" interpretation. However, standard English capitalization rules usually imply 'Sentence Case'.
             To strictly follow "first character ... is capitalized", we will uppercase the start and leave subsequent chars as-is or lowercase them?
             Let's assume standard behavior: Uppercase the starter, ensure it matches case if already upper (no change), 
             but do NOT capitalize intermediate words.

    Logic applied per instruction: First char of every word is capitalized. No other changes to existing casing unless specified.
    """
    result = []
    
    # Helper flag to track if we have started a new "word" block that needs capitalization logic on its first alpha character
    in_word_start = False
    
    for idx, char in enumerate(text):
        is_alnum = ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')
        
        if not is_alnum:
            # Non-alphanumeric character acts as word delimiter. 
            # We are no longer in the middle of a "word" for capitalization purposes regarding future chars, 
            # but we need to handle this non-alpha char correctly (append as is).
            result.append(char)
            
            # Check if next potential alphanumeric char will start a new word? No, just reset flag.
            continue
        
        in_word_start = True
        
        if idx == 0:
            # First character of entire string and not part of previous context (handled by logic below generally).
            result.append(char.upper())
        else:
            # Determine if this char starts a new word based on the immediate predecessor.
            is_prev_alnum = ('a' <= text[idx-1] <= 'z') or ('A' <= text[idx-1] <= 'Z') or ('0' <= text[idx-1] <= '9')
            
            # If previous char was not alphanumeric, this starts a new word.
            if not is_prev_alnum:
                result.append(char.upper())
            else:
                result.append(char)

    return ''.join(result)

# Final robust implementation combining clarity and efficiency
def capitalize_first_letter_only(text: str) -> str:
    """
    Returns a new string where only the first character of every word is capitalized.
    
    A "word" consists of one or more alphanumeric characters (a-z, A-Z, 0-9). 
    If two words are adjacent without non-alphanumeric separators, they are treated as separate words based on context?
    Usually in such problems: sequence [A][B] is not a word boundary unless separated by space/punctuation.
    So "AB" -> "Ab". 
    """
    
    # Build the result list of characters for efficiency (avoids repeated string concatenation)
    res = []
    
    n = len(text)
    if n == 0:
        return text
        
    i = 0
    
    while i < n:
        char = text[i]
        
        # Check if this character is part of a word (alphanumeric)
        def is_alnum(c):
            return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')

        if not char.isalnum():
            res.append(char)
            i += 1
            continue
            
        # If we are in the middle of a word (prev was alnum), just append as is? 
        # Wait, instruction: "only the first character ... is capitalized".
        # This implies if I have 'a', it becomes 'A'.
        
        # Let's trace logic properly.
        # We need to know if we are at the START of a word.
        # Start occurs when (i==0) OR text[i-1] was NOT alphanumeric.
        
        is_start = False
        
        # Special case for index 0, but handled by prev check conceptually? 
        # No direct access to i=-1. Handle separately or track state.
        if i == 0:
            is_start = True
            
        else:
            prev_char = text[i-1]
            if not is_alnum(prev_char):
                is_start = True
        
        # If it's the start of a word and has an uppercase/lowercase property (it must be alphanumeric)
        if is_start and 'a' <= char <= 'z':
            res.append(char.upper())
        elif is_start and ('A' <= char <= 'Z'):
             # It was already upper, keep it. But technically "capitalized" means set to title case? 
             # Usually just ensuring .upper() on the specific character if lowercased or keeping as is if upper.
             res.append(char)
        else:
            # Not start of word (continuation), or not a letter (digit/symbol already handled above).
            # If it's continuation, keep original case? 
            # Example "Hello World" -> "Hello World". "hello world" -> "Hello World"? No.
            # Strictly: first char capitalized. Rest unchanged? Or rest lowercased to avoid mixed case mid-word like 'aBcDe'?
            # Usually English capitalization rules apply (Sentence Case). 
            # But prompt says "only the first character ... is capitalized". 
            # Let's assume strict adherence: First -> Upper, Others -> Original.
            
            res.append(char)

        i += 1
        
    return ''.join(res)

if __name__ == '__main__':
    pass
