def compare_strings(str1: str, str2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and returns a tuple with:
        - 0 if they are equal (lexicographically), otherwise the sign of their difference.
          Negative means str1 < str2; positive means str1 > str2.
        - The integer difference between len(str1) and len(str2).

    Parameters:
        str1, str2: Input strings to compare.

    Returns:
        tuple[int, int]: (comparison_result, length_difference)
            comparison_result is 0 if equal, negative if str1 < str2, positive otherwise.
            length_difference = len(str1) - len(str2).
    """
    # Lexicographical comparison using standard string operators for clarity and robustness
    cmp_result: int
    try:
        result = (str1 > str2) * 1 + ((not (str1 < str2)) * -1 if str1 != str2 else 0)
        # Python's built-in comparison returns True/False. We map to numeric signs manually here for clarity, 
        # but a more direct approach using cmp_to_key or simply int() on the result logic below is safer:
        
        # Let's use a simpler explicit mapping based on standard behavior
        if str1 < str2:
            comparison_result = -1
        elif str1 > str2:
            comparison_result = 1
        else:
            comparison_result = 0
        
    except TypeError:
        # In case inputs are not comparable strings (though type hint says str)
        raise

    length_difference = len(str1) - len(str2)
    
    return comparison_result, length_difference

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies.
    s_a = "apple"
    s_b = "banana"

    result_cmp, diff_len = compare_strings(s_a, s_b)
    
    print(f"Comparing '{s_a}' and '{s_b}':")
    print(f"Lexicographical comparison: {result_cmp}")
    if result_cmp < 0:
        print("'apple' comes before 'banana' lexicographically.")
    elif result_cmp > 0:
        print("'apple' comes after 'banana' lexicographically.")
    else:
        print("The strings are equal.")

    print(f"Length difference (len(s_a) - len(s_b)): {diff_len}")