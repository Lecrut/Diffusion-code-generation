def compare_strings(str1: str, str2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and returns a tuple with:
        - Comparison result (0 if equal, 1 if str1 > str2, -1 otherwise)
        - Length difference (len(str1) - len(str2))

    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.

    Returns:
        tuple[int, int]: A tuple containing the comparison result and length difference.
    """
    # Lexicographical comparison using standard string operators which return -1 or 1 if not equal
    cmp_result = str1.__cmp__(str2)
    
    # Calculate length difference
    len_diff = len(str1) - len(str2)

    return (cmp_result, len_diff)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        ("apple", "banana"),
        ("hello", "world"),
        ("test", "test"),
        ("short", "longer string here"),
        ("z", "a"),
    ]

    print("String Comparison Results:")
    for s1, s2 in test_cases:
        result = compare_strings(s1, s2)
        cmp_outcome, length_diff = result
        
        # Determine textual outcome based on comparison value (-1 or 1)
        if cmp_outcome == -1:
            text_outcome = f"{s1} < {s2}"