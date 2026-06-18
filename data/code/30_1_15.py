def swap_adjacent_pairs(text: str) -> str:
    """
    Returns a new string where every pair of adjacent characters has been swapped.
    
    Uses slicing to process the string in steps of 2, swapping each (i, i+1).
    If an odd-length string ends with one character, it remains unchanged at the end.
    
    Args:
        text (str): The input string.
        
    Returns:
        str: A new string with adjacent pairs swapped.
    """
    result = []
    for i in range(0, len(text), 2):
        if i + 1 < len(text):
            # Swap the pair and append both characters
            result.append(text[i+1])
            result.append(text[i])
        else:
            # Odd character at the end remains as is
            result.append(text[i])
    return "".join(result)

if __name__ == '__main__':
    sample_input = "abcdef"
    output = swap_adjacent_pairs(sample_input)
    print(f"Input: '{sample_input}'")
    print(f"Output: '{output}'")

    # Additional test case for odd length string
    sample_input_2 = "abcdxyz"
    output_2 = swap_adjacent_pairs(sample_input_2)
    print(f"\nInput: '{sample_input_2}'")
    print(f"Output: '{output_2}'")