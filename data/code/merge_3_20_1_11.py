def case_insensitive_string_equal(str1: str, str2: str) -> bool:
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
        ("Hello", "hello"),
        ("HELLO WORLD!", "hELLO wORLD!"),
        ("Python 3.9", "python 3.9"),
        ("Different Strings", "different strings"),
        ("Same Case", "same case"),
    ]

    for i, (s1, s2) in enumerate(sample_cases):
        result = case_insensitive_string_equal(s1, s2)
        print(f"Test {i + 1}: '{s1}' == '{s2}' -> {result}")