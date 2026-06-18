from collections import Counter

def find_repeated_letters(text: str) -> set:
    """
    Returns a set of letters that appear more than once in the input string.
    
    The function is optimized by using collections.Counter, which runs in O(n) time
    where n is the length of the string, and uses hash tables for efficient lookups.

    Args:
        text (str): The input string to search for repeated letters.

    Returns:
        set: A set containing unique letter characters that appear more than once.
             Non-letter characters are ignored based on isinstance check for alphabets 
             if strict, but typically this means any character with a length > 1 count.
             
    Example:
        >>> find_repeated_letters("hello world")
        {'l', 'o'} (order may vary)

    Note: The function treats only characters present in the string as candidates.
          It includes all letters regardless of case sensitivity unless specified otherwise, 
          but typically we treat them case-insensitively for "letters" unless restricted to ASCII lowercase/uppercase distinctness? 
          
          Re-reading typical usage patterns implied here: return any character that repeats (case-sensitive).
          e.g., 'A' != 'a'. We count exact matches by char.

    If a user meant case-insensitive, they should pass the text.lower() explicitly if needed before passing to this function? 
    However, based on strict interpretation of "letters", we'll return characters (both letters and non-letters?)
    Wait: prompt says "find_repeated_letters". Should it only include alphabetic characters? Usually yes.

    Let's refine: We should filter for 'a' <= char <= 'z' or 'A' <= char <= 'Z'. 
"""

def find_repeated_letters(text):
    
    # Filter only letters to match the function name semantics (avoid digits/symbols unless specified)
    letter_chars = [char.lower() for char in text if char.isalpha()]

    count_map = Counter(letter_chars)
    
    repeated = {letter: True for letter, count in count_map.items()}
    
    # Return keys where count > 1. 
    return set([k for k,v in count_map.items() if v>1])

if __name__ == '__main__':
    sample_inputs = ["hello world", "aAaaBbBBcc", "!@#xyzXYZ"]

    for test_str in sample_inputs:
        result = find_repeated_letters(test_str)
        print(f"Input: {test_str!r} -> Repeated letters (lowercase normalized): {sorted(result)}")