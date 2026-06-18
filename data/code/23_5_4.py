def compare_strings(str1: str, str2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and returns a tuple with 
    (comparison_result, length_difference).
    
    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.
        
    Returns:
        tuple[int, int]: A tuple where the first element is -1 if str1 < str2, 
                         0 if str1 == str2, and 1 if str1 > str2. 
                          The second element is len(str1) - len(str2).
    """
    # Lexicographical comparison using standard string operators
    result = (str1 < str2) * (-1) + ((str1 > str2) * (1))
    
    # Calculate length difference: len(str1) - len(str2)
    length_diff = len(str1) - len(str2)
    
    return result, length_diff

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        ("apple", "banana"),
        ("zebra", "ant"),
        ("hello", "world"),
        ("test", "test"),
        ("shorter", "longest string here"),
    ]

    print("String Comparison Results:")
    for s1, s2 in test_cases:
        comparison_result, length_diff = compare_strings(s1, s2)
        
        # Determine the textual representation of the result (-1, 0, or 1)
        if comparison_result == -1:
            status = "str1 < str2"
        elif comparison_result == 0:
            status = "str1 == str2"
        else:
            status = "str1 > str2"
            
        print(f"'{s1}' vs '{s2}': {status}, Length Difference ({len(s1)} - {len(s2)}) = {length_diff}")