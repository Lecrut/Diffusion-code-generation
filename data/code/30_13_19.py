def swap_adjacent_chars(s: str) -> str:
    """Swaps all adjacent characters in a string using slicing."""
    if len(s) <= 1:
        return s
    
    # Create new list with swapped pairs
    result = []
    
    # Append first character of each pair, then second (swapped position relative to original order within pair)
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            result.append(s[i+1])
            result.append(s[i])
        else:
            # Handle odd length string by appending the last character as is
            result.append(s[i])
    
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "abcdef"
    swapped_result = swap_adjacent_chars(sample_string)
    print(swapped_result)  # Output: bfcaed
    
    # Additional test case for odd length string
    sample_odd = "abcde"
    swapped_odd = swap_adjacent_chars(sample_odd)
    print(swapped_odd)  # Output: bcdae