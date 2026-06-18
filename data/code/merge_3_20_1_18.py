def strings_equal_case_insensitive(str1: str, str2: str) -> bool:
    """
    Checks if two strings are equal in a case-insensitive manner.
    
    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.
        
    Returns:
        bool: True if the strings are equal ignoring case, False otherwise.
    """
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    # Sample test cases run without user input or command-line arguments
    test_cases = [
        ("Hello", "hello"),         # Should be True
        ("HELLO WORLD!", "hello world!"),  # Should be True
        ("Python", "pythonic"),     # Should be False
        ("", ""),                   # Edge case: Both empty, should be True
        ("Aa1b2Cc3Dd4Ee5Ff6Gg7Hh8Ii9Jj0Kk1Ll2Mm3Nn4Oo5Pp6Qq7Rr8Ss9Tt0Uu1Vv2Ww3Xx4Yy5Zz6", "Aa1b2Cc3Dd4Ee5Ff6Gg7Hh8Ii9Jj0Kk1Ll2Mm3Nn4Oo5Pp6Qq7Rr8Ss9Tt0Uu1Vv2Ww3Xx4Yy5Zz"), # Should be False (one char difference)
    ]

    for i, (s1, s2) in enumerate(test_cases, start=1):
        result = strings_equal_case_insensitive(s1, s2)
        print(f"Test {i}: \"{s1}\" vs \"{s2}\" -> Equal: {result}")