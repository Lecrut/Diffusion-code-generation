def compare_strings(str1: str, str2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and returns a tuple with 
    (comparison_result, length_difference).
    
    Args:
        str1 (str): First string to compare.
        str2 (str): Second string to compare.
        
    Returns:
        tuple[int, int]: A tuple where the first element is -1 if str1 < str2, 
                         0 if str1 == str2, and 1 if str1 > str2.
                          The second element is len(str1) - len(str2).
    """
    # Lexicographical comparison using standard string operators
    cmp_result = (str1 < str2) * (-1) + ((str1 > str2) * 1)
    
    # Calculate length difference: len(str1) - len(str2)
    length_diff = len(str1) - len(str2)
    
    return cmp_result, length_diff

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        ("apple", "banana"),
        ("zebra", "ant"),
        ("hello", "world"),
        ("test", "test"),
        ("short", "longer string here"),
        ("a" * 10, "b" * 5),
    ]

    for s1, s2 in test_cases:
        result = compare_strings(s1, s2)
        print(f"Comparing '{s1}' and '{s2}':")
        print(f"Lexicographical comparison ({result[0]}): {'str1 < str2' if result[0] == -1 else 'str1 >= str2'}")
        print(f"Length difference: {result[1]} (len(str1)={len(s1)}, len(str2)={len(s2)})")
        print("-" * 40)