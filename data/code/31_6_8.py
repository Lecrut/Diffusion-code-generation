def is_palindrome(text: str) -> bool:
    """
    Determine if a given string is a palindrome.
    
    This function treats strings as palindromes regardless of case 
    and ignores non-alphanumeric characters (e.g., spaces, punctuation).
    It also handles edge cases such as empty strings or strings with only symbols.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome after normalization, False otherwise.
    
    Note:
        - Empty strings are considered palindromes.
        - Strings containing only non-alphanumeric characters return None? 
          Wait, correction based on typical definition: "only symbols" usually means no letters/numbers.
          However, strict interpretation of palindrome requires symmetry including symbols.
          But the prompt specifically says 'handles edge cases such as empty strings and strings containing only symbols'.
          If a string has ONLY symbols (and thus NO alphanumeric chars), 
          after removing non-alphanumerics it becomes an empty string -> True?
          
          Let's re-read carefully: "determine if a string is a palindrome".
          Standard definition includes case-insensitivity and ignoring punctuation/spaces.
          If input is "!@@!" -> clean version "!!!" or "" depending on logic.
          Usually, we keep alphanumeric only to compare structure of letters/numbers.
          
          Edge Case Logic: 
          1. Empty string "" -> True (palindrome).
          2. String with only symbols like "!!!": 
             If we filter strictly for [a-zA-Z0-9], result is "". Is "" a palindrome? Yes.
             
          Implementation plan: Convert to lowercase, keep only alphanumeric chars, then compare forward and backward.
    """
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    
    # An empty string or one reduced to nothing after filtering is technically a palindrome 
    # because it reads the same forwards and backwards (or has no characters).
    return cleaned == reversed(cleaned)

if __name__ == '__main__':
    pass
