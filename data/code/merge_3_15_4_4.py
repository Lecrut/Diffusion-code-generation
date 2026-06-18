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
        ("Python 3.10", "python 3.10"),  # Should be True
        ("Different", "different"),   # Should be False (wait, this should be true) -> correction below
        ("Test Case", "TEST CASE"),     # Should be True
    ]

    # Corrected sample case logic for clarity in comments above
    test_pairs = [
        ("Hello", "hello"),      # Expected: True
        ("World!", "WORLD!"),    # Expected: True
        ("Python 3.10", "python 3.10"),  # Expected: True
        ("Different", "different"),   # Expected: True (corrected from comment)
        ("Test Case", "TEST CASE"),     # Expected: True
        
        ("Apple", "Banana"),      # Expected: False
    ]

    for i, (s1, s2) in enumerate(test_pairs):
        result = compare_strings(s1, s2)
        print(f"Test {i+1}: '{s1}' vs '{s2}' -> {result}")