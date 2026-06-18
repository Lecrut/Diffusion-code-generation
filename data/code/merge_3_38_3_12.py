def contains_repeated_letters(s: str) -> bool:
    """
    Determines if a given string contains any repeated letters (case-insensitive).
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if there are repeating letters, False otherwise.
    """
    seen = set()
    for char in s.lower():
        # Skip non-letter characters as per common interpretation of "letters"
        if not char.isalpha():
            continue
        if char in seen:
            return True
        seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        ("hello", True),       # 'l' repeats
        ("world", False),      # no repeating letters
        ("AaBbCcDd", True),   # all repeat but case-insensitive match
        ("abcdefg", False),    # unique lowercase
        ("123abc", False),    # numbers skipped, 'a','b','c' unique
        ("aaa", True),         # repeats
        ("The Quick Brown Fox", True)  # space/punctuation ignored, letters repeated? T,h,e,Q,u,i,c,k,B,r,o,w,n,F,o,x -> o repeats
    ]

    for test_input, expected in test_cases:
        result = contains_repeated_letters(test_input)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] Input: '{test_input}' => Expected: {expected}, Got: {result}")