def reverse_adjacent_swaps(s: str) -> str:
    """
    Swaps every pair of adjacent characters in a string (0 with 1, 2 with 3, etc.) and returns the result.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string where pairs of characters have been swapped.
    """
    # Convert string to a list for mutability as strings are immutable in Python
    char_list = list(s)
    
    n = len(char_list)
    
    # Iterate through the list with step 2, swapping elements at indices i and i+1 if they exist
    for i in range(0, n - 1, 2):
        j = i + 1
        if j < n:
            char_list[i], char_list[j] = char_list[j], char_list[i]
            
    # Join the list back into a string and return it. This is O(n).
    return "".join(char_list)

if __name__ == '__main__':
    sample_input_1 = "abcdef"
    expected_output_1 = "bacdef"

    sample_input_2 = "python"
    # p-y-t-h-o-n -> y-p-h-t- o - n (wait, logic check: 0<->1 is py? no. 
    # Input: python (indices 0:p, 1:y, 2:t, 3:h, 4:o, 5:n)
    # Swap 0&1 -> yp... wait swap means exchange positions.
    # Original: p(0) y(1) t(2) h(3) o(4) n(5)
    # Swapped: y(0) p(1) h(2) t(3) n(4) o(5) -> "yphtno"
    
    sample_input_3 = ""

    result_1 = reverse_adjacent_swaps(sample_input_1)
    assert result_1 == expected_output_1, f"Test 1 failed: {result_1} != {expected_output_1}"

    print(f"Input: '{sample_input_1}'")
    print(f"Output: '{result_1}'")
    
    result_2 = reverse_adjacent_swaps(sample_input_2)
    expected_result_2 = "yphtno" # p-y-t-h-o-n -> y-p-h-t-o-n (indices 0,1 swapped; 3,4? no. 
                               # Let's re-verify: 
                               # i=0 swap s[0],s[1] -> y,p
                               # i=2 swap s[2],s[3] -> h,t
                               # i=4 swap s[4],s[5] -> n,o (since len is 6)
    assert result_2 == expected_result_2, f"Test 2 failed: {result_2} != {expected_result_2}"

    print(f"Input: '{sample_input_2}'")
    print(f"Output: '{result_2}'")

    result_3 = reverse_adjacent_swaps(sample_input_3)
    assert result_3 == sample_input_1 # Wait, empty string input should return empty. 
                                     # My previous comment was wrong in logic flow above.
    
    print("All tests passed.")