def case_insensitive_equal(str1: str, str2: str) -> bool:
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
    # Sample test cases with hard-coded values
    sample_cases = [
        ("Hello", "hello"),       # Should be True
        ("HELLO WORLD!", "world hello!"),  # Should be False (length mismatch)
        ("Python", "python"),     # Should be True
        ("Case Insensitive Test", "CASE INSENSITIVE TEST"), # Should be True
        ("Different Strings", "different strings"),   # Should be True
        ("Test123", "test456"),  # Should be False (content differs)
    ]

    for i, (s_a, s_b) in enumerate(sample_cases):
        result = case_insensitive_equal(s_a, s_b)
        print(f"Case {i + 1}: '{s_a}' vs '{s_b}' -> {'Equal' if result else 'Not Equal'}")