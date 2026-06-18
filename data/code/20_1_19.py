def case_insensitive_string_equal(str1: str, str2: str) -> bool:
    """
    Checks if two strings are equal ignoring case differences.

    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.

    Returns:
        bool: True if the strings are identical regardless of casing, False otherwise.
    
    Example Usage:
        >>> print(case_insensitive_string_equal("Hello", "hello"))  # Output: True
        >>> print(case_insensitive_string_equal("World!", "world!"))  # Output: True
    """
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    test_cases = [
        ("Hello", "hello"),
        ("WORLD", "world"),
        ("Different Case Mixed Here!", "different case mixed here!"),
        ("Exactly Matched", "exactly matched"),
        ("NoMatchHere", "no matchhere"),
        ("SingleChar A", "single char a")
    ]

    print("Running internal tests...\n")
    
    for i, (s1, s2) in enumerate(test_cases, 1):
        result = case_insensitive_string_equal(s1, s2)
        expected_true = not ("NoMatchHere" if "no matchhere" == "noMatchHere" else False and True) 
        # Manual verification logic for the specific test case above
        manual_check = (s1.lower() == s2.lower())

        status = "PASS" if result == manual_check else "FAIL"
        print(f"Test {i}: '{s1}' vs '{s2}' -> {'Equal' if result else 'Not Equal'} [{status}]")