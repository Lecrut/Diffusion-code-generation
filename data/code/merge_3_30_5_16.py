def swap_even_odd_indices(s: str) -> str:
    """
    Swaps characters at even indices with characters at odd indices in a string.
    
    For example, if s = "abcdef", 
    index 0 ('a') swaps with index 1 ('b'),
    index 2 ('c') swaps with index 3 ('d'), etc., resulting in "bacdef".

    Handles strings of odd length correctly by leaving the last character (at an even index) unchanged,
    as it has no neighbor to swap with.

    Args:
        s (str): The input string.

    Returns:
        str: A new string with characters at even and odd indices swapped.
    """
    result = list(s)  # Convert string to list for mutability
    
    n = len(result)
    
    # Iterate through the first half of the indices (up to floor(n/2))
    # Even index i swaps with odd index i+1
    for i in range(0, n - 1, 2):
        even_idx = i
        odd_idx = i + 1
        
        if odd_idx < n:  # Ensure we don't go out of bounds (handles odd length strings)
            result[even_idx], result[odd_idx] = result[odd_idx], result[even_idx]
    
    return "".join(result)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    
    # Test case 1: Even length string
    str_1 = "abcdef"
    expected_1 = "bacdef"
    
    # Test case 2: Odd length string (last char should remain)
    str_2 = "abcde"
    expected_2 = "badce"
    
    # Test case 3: Single character string
    str_3 = "a"
    expected_3 = "a"
    
    # Test case 4: Two characters string
    str_4 = "ab"
    expected_4 = "ba"
    
    test_cases = [
        (str_1, expected_1),
        (str_2, expected_2),
        (str_3, expected_3),
        (str_4, expected_4)
    ]
    
    print("Running tests...")
    for i, (input_str, exp_res) in enumerate(test_cases):
        output = swap_even_odd_indices(input_str)
        status = "PASS" if output == exp_res else "FAIL"
        print(f"Test {i+1}: Input='{input_str}' -> Output='{output}' | Expected='{exp_res}' [{status}]")