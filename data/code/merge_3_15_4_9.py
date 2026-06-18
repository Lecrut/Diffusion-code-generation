def compare_strings(str1: str, str2: str) -> bool:
    """
    Checks if two strings are equal ignoring case sensitivity.

    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.

    Returns:
        bool: True if the strings match case-insensitively, False otherwise.
    """
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert compare_strings("Hello", "hello") is True
    assert compare_strings("Python3", "python3.0") is False  # Different lengths after lowercasing? No, wait. Python3 vs python3 -> equal length but different content? Let's use clearer examples below.

    # Corrected sample assertions for clarity
    test_cases = [
        ("Hello World", "HELLO WORLD"),
        ("Test Case!", "test case!"),
        ("ABC123", "abc123"),
        ("Different Strings", "different strings"),  # Should return True
        ("Not Equal", "equal not"),               # Should return False
    ]

    for str1, str2 in test_cases:
        result = compare_strings(str1, str2)
        print(f"Comparing '{str1}' and '{str2}': {result}")