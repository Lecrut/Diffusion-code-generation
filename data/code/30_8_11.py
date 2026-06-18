def swap_adjacent(s: str) -> str:
    """
    Swaps every pair of adjacent characters in a string if they exist.
    
    If the string length is even, all pairs are swapped (e.g., "ab" -> "ba").
    If the string length is odd, the last character remains unchanged 
    because it cannot form a complete pair with an index beyond the end.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with adjacent characters swapped at every even-odd index pair.
             Unpaired trailing character is omitted from swapping but retained 
             implicitly by not advancing past it in the iteration logic that forms pairs.
    
    Examples:
        >>> swap_adjacent("ab") -> "ba"
        >>> swap_adjacent("abc") -> "bac" (only 'a' and 'b' swapped, 'c' stays)
        >>> swap_adjacent("") -> ""
    """
    return ''.join(s[i] + s[i+1] if i < len(s)-1 else '' for i in range(0, len(s), 2))

if __name__ == '__main__':
    # Test Case 1: Even length string (pairs exist fully)
    test_even = "abcd"
    expected_result_1 = "bacd"
    
    result_1 = swap_adjacent(test_even)
    assert result_1 == expected_result_1, f"Test even failed. Expected {expected_result_1}, got {result_1}"

    # Test Case 2: Odd length string (last char remains fixed position relative to pair logic)
    test_odd = "abcde"