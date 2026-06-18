def swap_adjacent_chars(s: str) -> str:
    """
    Swaps adjacent characters in a string by iterating through it with step 2,
    exchanging every character at an even index (0-based) with the one immediately following it.
    
    If the string length is odd, the last character remains unchanged as there is no next character to swap with.

    Parameters:
        s (str): The input string containing any characters.

    Returns:
        str: A new string where adjacent pairs of characters have been swapped.
             For example, "abX" becomes "baX", and "abcdef" becomes "bacdef".
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")

    # Convert to list for mutability since strings are immutable in Python
    char_list = list(s)
    length = len(char_list)

    # Iterate over indices with step 2 and swap adjacent elements
    for i in range(0, length - 1, 2):
        if i + 1 < length:
            char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]

    # Join the list back into a string and return
    return "".join(char_list)

if __name__ == '__main__':
    # Test Case 1: Even length string (complete pairs to swap)
    input_str_1 = "abcdef"
    output_str_1 = swap_adjacent_chars(input_str_1)
    assert output_str_1 == "bacdef", f"Test case 1 failed. Expected 'bacdef', got '{output_str_1}'."

    # Test Case 2: Odd length string (last character should remain unchanged)
    input_str_2 = "abcde"
    output_str_2 = swap_adjacent_chars(input_str_2)
    assert output_str_2 == "bacd", f"Test case 2 failed. Expected 'bacd', got '{output_str_2}'."

    # Test Case 3: Even length string with repeated characters to verify logic holds for non-unique chars
    input_str_3 = "aabbccdd"
    output_str_3 = swap_adjacent_chars(input_str_3)
    assert output_str_3 == "baacbdcd", f"Test case 3 failed. Expected 'baacbdcd', got '{output_str_3}'."

    print("All test cases passed successfully.")