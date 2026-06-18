def reverse_adjacent_swaps(s: str) -> str:
    """
    Takes a string and swaps every pair of characters (index 0 with 1, 
    index 2 with 3, etc.) in-place logic applied to build the result.
    
    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(1) excluding output storage if modified list used, 
                       or O(n) for new string construction.

    Args:
        s (str): The input string to process.

    Returns:
        str: A new string with adjacent characters swapped in pairs.
    """
    chars = list(s)
    
    # Iterate over the string in steps of 2
    n = len(chars)
    for i in range(0, n - 1, 2):
        if i + 1 < n:
            # Swap current character with next one
            chars[i], chars[i + 1] = chars[i + 1], chars[i]

    return ''.join(chars)

if __name__ == '__main__':
    sample_input = "abcdef"
    result = reverse_adjacent_swaps(sample_input)
    print(f"Input: '{sample_input}'")
    print(f"Output: '{result}'")