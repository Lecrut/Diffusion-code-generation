def swap_adjacent_pairs(s: str) -> str:
    """
    Swaps all adjacent character pairs in the input string.
    
    The function iterates through the string with a step of 2. 
    If there are two characters at indices i and i+1, they are swapped.
    Odd-length strings will have the last character remain unchanged as it cannot form a pair.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with all adjacent pairs swapped in-place logic applied.
    """
    result = []
    # Iterate over the string in steps of 2
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            # Swap characters at current index and next index
            result.append(s[i + 1])
            result.append(s[i])
        else:
            # Append the last character as is if it doesn't have a pair
            result.append(s[i])
    return ''.join(result)

if __name__ == '__main__':
    sample_strings = [
        "abcdef",
        "aabbccdd",
        "xyz"
    ]

    for test_input in sample_strings:
        output = swap_adjacent_pairs(test_input)
        print(output)