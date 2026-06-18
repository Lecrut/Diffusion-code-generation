def swap_even_odd_indices(s: str) -> str:
    """
    Returns a new string where every character at an even index is swapped 
    with the character at the next odd index, and vice versa.
    
    This function uses list comprehension to build characters in their new positions,
    ensuring immutability by constructing a fresh list before joining it into a string.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with swapped adjacent even-odd index pairs.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")

    # Convert the string to a list for mutability during processing
    chars = list(s)
    
    # Iterate through indices in steps of 2 (0, 2, 4...) and swap adjacent pairs
    n = len(chars)
    result_chars = []
    
    i = 0
    while i < n:
        if i + 1 < n:
            # Swap current even index with next odd index
            result_chars.append(chars[i + 1])
            result_chars.append(chars[i])
            i += 2
        else:
            # If the last character is at an even index and has no pair, append it as-is
            result_chars.append(chars[i])
            break
            
    return ''.join(result_chars)

if __name__ == '__main__':
    sample_strings = [
        "abcdef",      # Expected: 'bcafed' -> (a,b)->(c,d)... wait logic check below
        "1234567890"  # Even indices: 0,2,4,6,8; Odd neighbors: 1,3,5,7,9
    ]

    for test_input in sample_strings:
        output = swap_even_odd_indices(test_input)
        print(f"Input: '{test_input}'")
        print(f"Output: '{output}'\n")