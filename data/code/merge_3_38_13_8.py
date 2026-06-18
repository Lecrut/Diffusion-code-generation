def contains_repeated_letters(text: str) -> bool:
    """
    Determines if a given string contains any repeated letters (case-insensitive).
    
    Args:
        text (str): The input string to check.
        
    Returns:
        bool: True if there are duplicate letters, False otherwise.
    """
    seen = set()
    for char in text.lower():
        # Only consider alphabetic characters; ignore digits and symbols based on typical interpretation of "letters"
        if 'a' <= char <= 'z':
            if char in seen:
                return True
            seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        ("hello", True),
        ("abcdefg", False),
        ("A man, a plan, a canal: Panama", True),  # 'a' and 'n' repeat case-insensitively if considered letters only; here we check strictly alphabetic chars. Note: ':' is ignored per logic above but spaces too. Actually in this specific string 'P','a','m','e','r':' (colon) etc - let's trace manually for sample correctness below).
        # Correction on manual trace for "A man, a plan, a canal: Panama": 
        # Lowercase without non-letters: 'amanaplanacanalanpanama' -> many repeats like 'a', 'n'. Should be True.
    ]

    print("Testing contains_repeated_letters function:")
    all_passed = True
    for i, (input_str, expected) in enumerate(test_cases):
        result = contains_repeated_letters(input_str)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"Test {i+1}: '{input_str}' -> Expected {expected}, Got {result} [{status}]")

    if all_passed:
        print("\nAll tests passed.")
    else:
        print("\nSome tests failed.")