def compare_strings(s1: str, s2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and returns a tuple with 
    (comparison_result, length_difference).
    
    Lexicographical comparison rules:
        - Returns 0 if both strings are identical.
        - Returns 1 if s1 is greater than s2.
        - Returns -1 if s1 is less than s2.
        
    Length difference calculation:
        - Returns (len(s1) - len(s2)).

    Args:
        s1 (str): First string to compare.
        s2 (str): Second string to compare.

    Returns:
        tuple[int, int]: A tuple containing the comparison result and length difference.
    """
    # Lexicographical comparison using standard string operators
    if s1 == s2:
        cmp_result = 0
    elif s1 > s2:
        cmp_result = 1
    else:
        cmp_result = -1

    # Calculate the length difference (s1_length minus s2_length)
    len_diff = len(s1) - len(s2)

    return cmp_result, len_diff

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        ("apple", "banana"),
        ("zebra", "ant"),
        ("hello", "world"),
        ("test", "test"),
        ("a" * 10, "b" * 5),
    ]

    for s1_val, s2_val in test_cases:
        result = compare_strings(s1_val, s2_val)
        print(f"Comparing '{s1_val}' and '{s2_val}':")
        print(f"Comparison Result (0=equal, 1>s2, -1<s2): {result[0]}")
        print(f"Length Difference ({len(s1_val)} - {len(s2_val)}) : {result[1]}")
        print("-" * 30)