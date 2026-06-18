def swap_adjacent_pairs(s: str) -> str:
    """
    Swaps every pair of adjacent characters in a string using slicing.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with adjacent pairs swapped. If the length is odd, 
             the last character remains unchanged.
    """
    # Slice every two characters starting from index 1 and step by 2
    reversed_pairs = s[1::2] + s[0::2]
    
    return "".join(reversed_pairs)

if __name__ == '__main__':
    sample_inputs = [
        "abcdef",
        "aabbccdd",
        "python"
    ]

    for test_input in sample_inputs:
        result = swap_adjacent_pairs(test_input)
        print(f"Input: {test_input}")
        print(f"Output: {result}\n")