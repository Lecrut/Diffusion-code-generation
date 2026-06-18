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
    samples = [
        ("Hello", "hello"),
        ("HELLO WORLD!", "world! hello"),
        ("Python 3.9", "python 3.9"),
        ("Different Strings", "different strings"),
        ("", ""),
        ("Case Mismatch", "case mismatch"),
    ]

    for i, (s1, s2) in enumerate(samples):
        result = case_insensitive_equal(s1, s2)
        print(f"Test {i + 1}: '{s1}' == '{s2}' -> {result}")