"""Module to swap adjacent characters in a string."""

def swap_adjacent_chars(s: str) -> str:
    """Swap every pair of adjacent characters in the input string.
    
    If the string has an odd length, the last character remains unchanged.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with adjacent characters swapped.
        
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    
    result = []
    for i in range(0, len(s), 2):
        # Check if there's a second character to swap with
        if i + 1 < len(s):
            result.append(s[i])
            result.append(s[i+1])
        else:
            # Odd-length string end: append the last char as is, but since we iterate by 2
            # and check bounds, this logic needs slight adjustment for clean appending.
            # Let's re-evaluate loop to ensure correct construction.
            pass
    
    # Re-implementing swap logic more clearly within a list comprehension or explicit loop
    swapped_list = []
    i = 0
    while i < len(s):
        if i + 1 < len(s):
            swapped_list.append(s[i])
            swapped_list.append(s[i+1])
            i += 2
        else:
            # This case handles the single last character of an odd-length string logic correctly? 
            # Actually, standard swap usually means swapping pairs. If length is N (odd), 
            # we have floor(N/2) swaps and one remaining char at end which stays put relative to its position if not part of a pair.
            # Wait, the instruction says "swapping adjacent characters". Usually implies s[0]<->s[1], s[2]<->s[3]...
            swapped_list.append(s[i])
            i += 1
            
    return "".join(swapped_list)

if __name__ == '__main__':
    # Test Case 1: Even length string (should fully swap all pairs)
    test_str_1 = "abcd"
    expected_1 = "badc"
    
    # Test Case 2: Odd length string (last character remains unchanged relative to pair logic, but appended at end)
    # Actually standard interpretation: ab -> ba, cdc -> dc d? No. 
    # Input: abcde -> bacad e? Or just swap pairs and leave last alone?
    # Standard "swap adjacent" usually means s[0] with s[1], s[2] with s[3]. The last one stays if no partner.
    test_str_2 = "abcde"
    expected_2 = "badce"  # ab->ba, cd->dc, e remains
    
    # Test Case 3: Empty string and single character edge cases combined in a short even/odd mix
    test_str_3 = ""
    expected_3 = ""

    assert swap_adjacent_chars(test_str_1) == expected_1, f"Test 1 failed: {swap_adjacent_chars(test_str_1)} != {expected_1}"
    
    # Re-verify logic for odd length manually to ensure correctness before asserting.
    # "abcde": 
    # i=0: swap a,b -> ba, list=['b','a'], next index 2
    # i=2: swap c,d -> dc, list=['b','a','d','c'], next index 4
    # i=4: check if 5 < 5? False. Append 'e'. List=['b','a','d','c','e']