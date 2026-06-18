def compare_strings(s1: str, s2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and returns a tuple with 
    (comparison_result, length_difference).
    
    Args:
        s1 (str): First string.
        s2 (str): Second string.
        
    Returns:
        tuple[int, int]: A tuple where the first element is -1 if s1 < s2, 0 if equal, 
                         and 1 if s1 > s2 lexicographically. The second element is 
                         len(s1) - len(s2).
    """
    # Lexicographical comparison using Python's built-in string comparison logic
    lex_result = (s1 < s2) * (-1) + ((s1 == s2)) * 0 + (s1 > s2) * 1
    
    length_difference = len(s1) - len(s2)
    
    return lex_result, length_difference

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        ("apple", "banana"),
        ("zebra", "ant"),
        ("hello", "world"),
        ("test", "test"),
        ("shorter", "longer string here")
    ]

    print("String Comparison Results:")
    for s1, s2 in test_cases:
        result = compare_strings(s1, s2)
        lex_status = "<" if result[0] == -1 else "=" if result[0] == 0 else ">"
        length_diff_str = f"{result[1]}"
        
        print(f"'{s1}' vs '{s2}': Lexicographical {lex_status}, Length Difference: {length_diff_str}")