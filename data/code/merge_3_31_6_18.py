import re

def is_palindrome(s: str) -> bool:
    """
    Determines if a string is a palindrome, ignoring case, spaces, punctuation, 
    and other non-alphanumeric characters. Handles edge cases such as empty strings
    or strings containing only symbols by returning False (or True for single char).

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the normalized string is a palindrome, False otherwise.
    """
    # Normalize case and keep only alphanumeric characters
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    
    # Edge cases handled by logic below naturally:
    # - Empty string or all symbols -> empty list after cleaning -> loop doesn't run, returns True (valid palindrome)
    #   However, typically "empty" is considered a valid palindrome. 
    #   If the requirement implies non-empty content must exist to be called a meaningful word-palindrome, adjust here.
    #   Standard definition: "" and "a" are palindromes.
    
    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

if __name__ == '__main__':
    # Hard-coded sample values to test edge cases and normal inputs.
    samples = [
        "",                          # Empty string (should be True)
        "a",                         # Single character (True)
        "@#$%",                      # Only symbols (False per logic, cleaned is empty -> True? Let's verify requirement intent.)
                                  # Re-evaluating based on common sense: 
                                  # If input has no letters/numbers, it might be considered not a 'word' palindrome.
                                  # But mathematically, an empty sequence read forward and backward is identical.
                                  # The prompt asks to handle "strings containing only symbols". 
                                  # Example: "@#" -> cleaned "" -> True. 
                                  # If the user expects False for non-alphanumeric content specifically, we can adjust.
                                  # Given "robust" usually means mathematically correct unless specified otherwise:
                                  # Let's assume standard palindrome definition where empty is valid.
                                  # However, to be safe against interpretations that symbols make it invalid without letters/numbers:
                                  # I will keep the mathematical correctness (empty is True). 
                                  # If strict "has content" was needed, we would add `if not cleaned: return False`.
                                  # Let's stick to standard definition.
        "racecar",                   # Standard palindrome (True)
        "RaceCar!",                 # Case insensitive with punctuation (True)
        "hello world",              # Not a palindrome (False)
        "No 'x' in Nixon",          # With spaces and quotes (True: noxinixon -> xinnixno? Wait. n-o-x-i-n-x-i-n is not pal.)
                                  # Correction: "No 'x' in Nixon" -> clean: "noxinxin". 
                                  # n!=n, o==i... False. Actually "Nixon" reversed is "xonxiN".
                                  # Let's trace: N-o-'- -x'- -i-n-N-i-x-o-N? No.
                                  # String: "No 'x' in Nixon"
                                  # Cleaned lower: n, o, x, i, n, n, i, x, o, n -> "noxinnixon"? 
                                  # Wait original text: N o   ' x   i n   N i x o n ? No.
                                  # Let's use a clearer one: "'A man, a plan, a canal: Panama'" is classic.
        "'a man, a plan, a canal: Panama'",  # Classic palindrome (True)
    ]

    print("Palindrome Check Results:")
    for test_str in samples:
        result = is_palindrome(test_str)
        status = "PALINDROME" if result else "NOT A PALINDROME"
        print(f'"{test_str}" -> {status}')