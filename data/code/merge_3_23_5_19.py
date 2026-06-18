def compare_strings(str1: str, str2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and returns a tuple with 
    (comparison_result, length_difference).
    
    Comparison logic:
        - If str1 < str2 lexically: comparison_result = -1
        - If str1 > str2 lexically: comparison_result = 1
        - Otherwise: comparison_result = 0
    
    Length difference is calculated as len(str1) - len(str2).
    
    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.
        
    Returns:
        tuple[int, int]: A tuple containing the comparison result and length difference.
    """
    # Lexicographical comparison using Python's built-in < operator which handles Unicode correctly
    if str1 < str2:
        cmp_result = -1
    elif str1 > str2:
        cmp_result = 1
    else:
        cmp_result = 0
    
    length_diff = len(str1) - len(str2)
    
    return (cmp_result, length_diff)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        ("apple", "banana"),      # Lexicographically smaller, different lengths
        ("zebra", "ant"),         # Lexicographically larger, same length (4 vs 3) -> wait: zebra(6), ant(3)
        ("hello", "world"),       # Different first letters
        ("test", "testing"),      # Prefix case
        ("a", "aa"),              # Same start, different lengths
    ]

    for s1, s2 in test_cases:
        result = compare_strings(s1, s2)
        print(f"Comparing '{s1}' and '{s2}':")
        print(f"  Lexicographical comparison: {result[0]} (negative means str1 < str2)")
        print(f"  Length difference ({len(s1)} - {len(s2)}): {result[1]}")
        print()