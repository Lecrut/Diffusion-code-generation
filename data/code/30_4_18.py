def reverse_adjacent_swaps(s: str) -> str:
    """
    Swaps every pair of adjacent characters in the string (0-1, 2-3, etc.).
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string with all even-indexed and odd-indexed pairs swapped.
    """
    if len(s) == 0:
        return s
    
    # Convert the string to a list for mutability, as strings are immutable in Python.
    chars = list(s)
    
    # Iterate through indices with step size of 2 (start at 0, then skip by 2).
    for i in range(0, len(chars), 2):
        # Ensure we don't go out of bounds if the string length is odd.
        next_idx = min(i + 1, len(chars)) - 1
        
        # Swap characters at current position and previous (odd) index to avoid 
        # double swapping when step size > 0 in a standard loop structure?
        
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            chars[i], chars[i+1] = chars[i+1], chars[i]

    return ''.join(chars)

if __name__ == '__main__':
    # Sample test cases with hard-coded values.
    
    sample_1 = "abcdef"
    expected_1 = "bacdfeghijklmnopqrstu-vwx"  # Wait, let's fix the logic first based on requirement: swap every pair (0<->1, 2<->3). 
    # Input: a b c d e f -> Output: b a d c f e
    
    sample_1 = "abcdef"
    result_1 = reverse_adjacent_swaps(sample_1)
    
    print(f"Input: {sample_1}")
    print(f"Output: {result_1}")  # Expected: bacdfeghijklmnopqrstu-vwx is wrong, correct expected for 'abcdef' is 'bacfed'.
    # Correct logic check: 
    # a b c d e f -> swap(0,1)->ba; swap(2,3)->dc; (4,5) remains fe. Result: bacdef? No wait.
    # Indices 0(a), 1(b). Swap -> b,a.
    # Indices 2(c), 3(d). Swap -> d,c.
    # Indices 4(e), 5(f). Swap -> f,e.
    # Final string: "bacdf" + nothing? Wait, index 6 is end of 'abcdef' (length 6)? No indices are 0..5.
    # So b,a,d,c,f,e => "badcf"? Wait no. 
    # Let's trace manually:
    # i=0: swap s[0],s[1] -> a,b becomes b,a. List: [b, a, c, d, e, f]
    # i=2: swap s[2],s[3] -> c,d becomes d,c. List: [b, a, d, c, e, f]
    # i=4: swap s[4],s[5] -> e,f becomes f,e. List: [b, a, d, c, f, e]
    # Join -> "badcfe".
    
    print(f"Expected: badcfe")

    sample_2 = "12345"  # Odd length
    result_2 = reverse_adjacent_swaps(sample_2)
    expected_2 = "21435"
    print(f"\nInput: {sample_2}")
    print(f"Output: {result_2}")
    print(f"Expected: {expected_2}")

    sample_3 = ""  # Empty string
    result_3 = reverse_adjacent_swaps(sample_3)
    expected_3 = ""
    print(f"\nInput: '{sample_3}'")
    print(f"Output: '{result_3}'")
    print(f"Expected: '{expected_3}'")

    # Verification logic inside main block to ensure correctness based on O(n) constraint.
    if result_1 == "badcfe":
        print("\n[TEST PASSED] Sample 1 passed.")
    else:
        print("[ERROR] Sample 1 failed.")

    if result_2 == expected_2:
        print(f"[TEST PASSED] Sample 2 passed.")
    else:
        print([f"Sample 2 failed. Got {result_2}, Expected {expected_2}"]) # Note square brackets removed for valid string repr in f-string

    if result_3 == expected_3:
        print("[TEST PASSED] Sample 3 (empty) passed.")
    else:
        print("[ERROR] Sample 3 failed.")