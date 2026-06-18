def swap_adjacent_pairs(s: str) -> str:
    """
    Swaps all adjacent character pairs in the input string.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with every pair of characters swapped.
             If an odd number of characters exists, the last one remains unchanged.
    """
    result = []
    i = 0
    
    # Iterate through the string in steps of 2
    while i < len(s):
        if i + 1 < len(s):
            # Swap current character with next character and append to list
            pair = [s[i], s[i+1]]
            result.append(pair[1])
            result.append(pair[0])
            i += 2
        else:
            # Handle the case where there is an odd number of characters (last char)
            result.append(s[i])
            break
            
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "abcdef"
    
    # Process the hard-coded sample input
    modified_string = swap_adjacent_pairs(sample_input)
    
    # Print the result to standard output
    print(modified_string)