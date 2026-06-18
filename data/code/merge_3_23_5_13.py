def compare_strings(str1: str, str2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and returns a tuple with 
    (comparison_result, length_difference).
    
    Comparison logic:
        - Returns 0 if both strings are identical.
        - Returns 1 if str1 is greater than str2.
        - Returns -1 if str1 is less than str2.
        
    Length difference calculation:
        - Returns len(str1) - len(str2).

    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.

    Returns:
        tuple[int, int]: A tuple containing the comparison result and length difference.
    """
    if str1 == str2:
        return 0, len(str1) - len(str2)
    
    # Lexicographical comparison using standard operators
    cmp_result = (str1 > str2) - (str1 < str2)
    length_diff = len(str1) - len(str2)
    
    return int(cmp_result), length_diff

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        ("apple", "banana"),
        ("zebra", "ant"),
        ("hello world", "hello world"),
        ("test", "testing"),
        ("a" * 10, "b" * 5),
    ]

    for s1, s2 in test_cases:
        result = compare_strings(s1, s2)
        print(f"Comparing '{s1}' and '{s2}':")
        print(f"Comparison Result (lexicographical): {result[0]}")
        print(f"Length Difference ({len(s1)} - {len(s2)}): {result[1]}")
        print("-" * 30)