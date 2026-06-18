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
    sample_cases = [
        ("Hello", "hello"),      # Should be True
        ("World!", "WORLD!"),    # Should be True
        ("Python3.10", "python3.10"),  # Should be True
        ("Test", "test case"),   # Should be False
        ("", ""),                # Edge case: empty strings, should be True
        ("A" * 100, "a" * 100), # Long string test, should be True
    ]

    for i, (s1, s2) in enumerate(sample_cases):
        result = compare_strings(s1, s2)
        print(f"Test case {i + 1}: '{s1}' vs '{s2}' -> {result}")