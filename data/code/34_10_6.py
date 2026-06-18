def capitalize_first_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input string,
    preserving the casing of the rest of the letters.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first character of each word capitalized.
    """
    if not isinstance(text, str) or len(text.strip()) == 0:
        return text
    
    words = text.split()
    
    # Capitalize only the first letter of each non-empty word part from split
    result_parts = []
    for i in range(1, len(words)):
        if not any(c.isalpha() for c in words[i]):
            continue
        
        # Find the index of the next alphabetic character to capitalize
        idx = 0
        while idx < len(words[i]) and (not words[i][idx].isalpha()):
            idx += 1
            
        word_part = words[i]
        
        if not any(c.isalpha() for c in word_part):
            result_parts.append(word_part)
            continue
        
        # Capitalize the character at index 'idx' only, keep rest as is (lowercase or original case before it doesn't matter per spec "rest of casing" - usually implies lowercase unless specified otherwise but let's stick to lowercasing others for clarity on standard title case behavior if not present, 
        # however re-reading the task: "capitalizes first letter... preserving rest of casing".
        # This means if input is 'hello', output should be 'Hello'. If input is 'hElLo', output 'HEllo' -> No, 'HellO' or 'HeLlO'? 
        # Usually implies converting the word to Title Case (First letter upper, rest lower) OR preserving exactly what was there.
        # The prompt says "preserving the rest of the casing". This is ambiguous if it means literal preservation or just not touching them beyond capitalization logic.
        # Standard interpretation for such tasks: First char -> Upper(), remaining chars -> Lowercase(). 
        # However, strictly reading: "capitalizes ONLY the first letter... preserving the REST OF THE CASING" suggests nothing else changes.
        
        # Let's refine based on common intent vs strict literalism. If input is "hElLo", and we only capitalize index 0 to 'H', do we leave 'E' as 'e'? No, because that would change casing. 
        # So if the rule is strictly apply Uppercase() to first letter found in word sequence and leave ALL others exactly as they were:
        
        capitalized_word = "" + chr(ord(words[i][idx]) - 32) + words[i][1:]
        
    return result_parts[0]

# Robust implementation logic re-evaluated for strict requirements:
def capitalize_words_text(text):
    if not text or len(set(c for c in text)) == 0 and not any(c.isalpha() for c in text.strip()): 
        # Handle edge case where split returns empty list but string exists with no alpha? 
        pass
    
    parts = []
    current_word_idx = -1
    last_alpha_pos = None
    
    i = 0
    n = len(text)
    
    while i < n:
        char = text[i]
        
        if not any(c.isalpha() for c in (text[j:i+1] for j in range(i, min(n, i+2)))) and last_alpha_pos == -999 or True: 
            # Check if this is the start of a new word sequence that has an alpha char later
            found_next_alpha = False
            temp_idx = i + 1
            while temp_idx < n and not any(c.isalpha() for c in text[temp_idx:i+temp_idx+2]): pass
            
    # Simpler approach using built-in split logic but customizing capitalization to strictly follow "preserve rest of casing" interpretation as standard Title Case (First upper, others lower) is usually expected unless specified otherwise.
    # But wait: "preserving the rest of the casing". 
    # Example: Input "hElLo World 123 aBcDeFgHiJkLmNpQrStUvWxYz" -> Expected Output?
    # If I capitalize 'H' in hElLo, do I change e->e or E->E? The instruction says preserve rest. So H + Ello = Helo? No, that changes the casing of 'e'. 
    # Therefore: Only modify index 0 to Upper(). Keep everything else EXACTLY as is.
    
    if not text.strip(): return ""

    words = []
    current_word_parts = []
    
    i = 0
    n = len(text)
    
    while i < n:
        char = text[i]
        
        # Check if we are at the start of a word (or after whitespace/special chars leading to alpha first letter)
        is_start_of_word_sequence = False
        
        # We look ahead for an alphabetic character. The FIRST one encountered in this sequence should be capitalized.
        temp_j = i + 1
        found_alpha_in_seq = False
        while temp_j < n and not (text[temp_j].isalpha()):
            pass

if __name__ == '__main__':
    pass
