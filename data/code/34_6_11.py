"""
Performance-focused solution to capitalize the first letter of a string.
Handles edge cases such as empty strings, leading whitespace, 
and non-alphabetic characters in the beginning.
Complexity: O(n) time, O(1) extra space (excluding result).
"""

def capitalize_first_letter(text: str) -> str:
    """
    Capitalizes only the first alphabetic character found in the string.
    Leaves all other characters unchanged, including punctuation and whitespace.

    Args:
        text (str): The input string to process.

    Returns:
        str: A new string with only the first letter capitalized if it exists; otherwise returns original.
    """
    # Find index of the first alphabetic character
    idx = -1
    for i, char in enumerate(text):
        if 'a' <= char.lower() <= 'z':  # Check ASCII letters to ensure efficiency and correctness across locales if needed
            idx = i
            break
    
    # If no letter found or string is empty/only non-letters, return original (or handle per strict interpretation)
    # Based on "capitalize first letter only": if no letter exists, nothing changes. 
    # However, standard behavior often implies capitalizing the whole thing if it's a title case scenario, but here strictly 'first letter'.
    
    if idx == -1:
        return text

    # Construct result efficiently by slicing and concatenation (Python strings are immutable)
    first_char = text[idx].upper()
    rest_of_string = ""
    
    for j in range(idx + 1, len(text)):
        char = text[j]
        
        if 'a' <= char.lower() <= 'z':
            # Only capitalize the very first letter found. The prompt says "capitalize the first letter only". 
            # This implies subsequent letters remain as they are (lowercase or uppercase).
            rest_of_string += char.upper() if j == idx else char
        
        elif 'A' <= char.lower() < 'Z':  # Wait, logic above covers all alpha. Let's re-verify requirement.
            pass

    # Re-evaluating the requirement "capitalize the first letter only": 
    # Interpretation A: Capitalize index[0] if it is a letter. Leave rest as is.
    # Interpretation B: Find first letter, capitalize that one, leave everything else (including other letters) exactly as they were? Or do subsequent letters get lowercased or remain case-sensitive?
    # Usually "capitalize the word" implies Title Case logic for internal words too if specified, but here it says "first letter only". 
    # Strict reading: Only change the character at index 0 (if alpha). All others untouched.
    
    return text[:idx] + first_char + text[idx+1:]

def optimize_capitalize_first(text):
    """Optimized version using string formatting which is implemented in C."""
    if not text:
        return text
    
    # Find the index of the first alphabetic character efficiently
    idx = 0
    while idx < len(text) and not ('a' <= text[idx] <= 'z' or 'A' <= text[idx] <= 'Z'):
        idx += 1
        
    if idx == 0:
        # If it's the very first char of string (and it is a letter), capitalize it in-place conceptually via slice concat. 
        return f"{text[0].upper()}{text[1:]}"
    
    # Wait, re-reading "capitalize the first letter only". 
    # Does it mean: take the whole string, find the FIRST LETTER (e.g., 'hello world!' -> 'Hello world!'), or just capitalize character at 0?
    # Context of such tasks usually implies finding the next token's start. But without word boundaries defined, "first letter" is ambiguous between "char at index 0 if alpha" and "the first alphabetic char in string regardless of position".
    # Given edge cases like punctuation: 'a1b' -> ? 
    # If I capitalize strictly the *letter* (anywhere), then a non-letter prefix should be skipped.
    # Example: '!abc' -> 'Abc'. Or just '!ABC'? No, "first letter only". So likely 'A', rest unchanged? Or all subsequent letters lowercase? 
    # Let's assume standard behavior for such utility functions often seen in coding challenges:
    # Find first alpha char index i. Capitalize text[i]. Leave everything else EXACTLY as is (case preserved).
    
    if idx > 0 and ('a' <= text[idx] <= 'z'):
        return f"{text[:idx]}{text[idx].upper()}{text[idx+1:]}"

    # Fallback: If the requirement implies only index 0 matters regardless of being a letter? 
    # "capitalize the first letter" -> if string starts with non-letter, is there no 'first letter'?
    # Let's stick to finding the actual alphabetic character.
    
    return text

def solve_capitalize_first(text: str) -> str:
    """
    Final robust implementation based on strict interpretation: 
    Identify the first occurrence of an alphabetical character in the string.
    Capitalize THAT specific letter only. Do not modify any other characters (including subsequent letters or punctuation).
    
    Example logic trace:
    "hello" -> "Hello"
    "!abc" -> "Abc"  <-- First alpha found at index 1, capitalized to A. Rest 'bc' remains lowercase? Or unchanged? 
                   Strictly speaking "first letter only" means ONLY that one changes state from lower->upper or upper->lower (usually up). 
                   So '!aBc' -> '!AbC'? No, usually these tasks imply Title Case for the word but here it's raw string.
                   Let's assume: Only change case of identified char to UPPER. Others stay exactly as input? 
                   Or standard convention is lowercased everything else if not specified? 
                   Given "only", I will NOT lowercase others unless they are part of a title-case normalization which isn't requested.
    
    Revised Plan for strict adherence to text:
    1. Find index i where text[i] is alpha.
    2. If exists, capitalize it (upper()).
    3. Return string with this char changed, others identical? 
       OR return title case of the whole thing if that's what "capitalize" implies in common parlance?
       
       Let's look at edge cases: empty -> "". Punctuation -> skip until letter.
       
       Implementation decision: 
       Find first alpha index i. Cap text[i] to upper(). Leave rest exactly as is (preserving case of subsequent letters). 
       This seems the most literal interpretation of "first letter only". If they wanted Title Case, they'd say "capitalize each word" or similar.
    """
    
    # Handle empty string immediately for performance and clarity
    if not text:
        return ""

    idx = -1
    length = len(text)
    
    # Iterate to find the first alphabetic character
    for i in range(length):
        char_code = ord(text[i])
        # Check ASCII letters (a-z, A-Z) for simplicity and speed without locale dependencies unless specified otherwise. 
        if 97 <= char_code <= 122 or 65 <= char_code <= 90:
            idx = i
            break
    
    if idx != -1:
        # Replace only the character at found index with its uppercase version
        return text[:idx] + text[idx].upper() + text[idx+1:]

    else:
        # No alphabetic characters found, return original string (per strict logic) 
        # Or could be interpreted as "capitalize if possible", but here no letter exists.
        return text

if __name__ == '__main__':
    pass
