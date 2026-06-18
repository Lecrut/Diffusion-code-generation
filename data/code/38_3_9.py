def has_repeated_letters(text: str) -> bool:
    """
    Determines if a given string contains any repeated letters (case-insensitive).

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if there are duplicate letters, False otherwise.
    """
    seen = set()
    for char in text.lower():
        # Ignore non-letter characters as per the requirement context ("letters")
        if not 'a' <= char <= 'z':
            continue
        if char in seen:
            return True
        seen.add(char)
    return False

if __name__ == '__main__':
    sample_strings = [
        "abc",      # No repeats -> False
        "hello",     # 'l' repeated, 'o' repeated -> True
        "The quick brown fox",  # All unique letters (case-insensitive) -> True? Wait: e appears twice. So True
        "abcdefgxyzuvwlmn"   # Unique -> False, note m,n appear in context but here distinct from standard alphabet check logic. Let's re-verify manually for sample. 
                          # a,b,c,d,e,f,g,x,y,z,u,v,w,l,m,n - all unique? Yes. -> False
        "aabb",      # 'a' and 'b' repeated -> True
    ]

    for test_input in sample_strings:
        result = has_repeated_letters(test_input)
        print(f"'{test_input}': {result}")