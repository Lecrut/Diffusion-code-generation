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
    # Sample test cases running without user input or external dependencies
    sample_cases = [
        ("Hello", "hello"),
        ("HELLO WORLD!", "hElLo WoRlD!"),
        ("Python 3.10", "python 3.10"),
        ("Different Strings", "different strings"),
        ("Case Sensitive Test", "case sensitive test"),
    ]

    for i, (s_a, s_b) in enumerate(sample_cases):
        result = case_insensitive_equal(s_a, s_b)
        print(f"Test {i + 1}: '{s_a}' == '{s_b}' -> {result}")