def swap_adjacent_chars(s: str) -> str:
    """
    Swaps all adjacent characters in a string using list manipulation and slicing.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with every pair of adjacent characters swapped.
             If the length is odd, the last character remains unchanged.
    """
    if not s:
        return ""

    # Convert to list for mutability (more efficient than repeated slicing)
    char_list = list(s)
    
    # Iterate through the list with a step of 2 and swap elements at index i and i+1
    for i in range(0, len(char_list), 2):
        if i + 1 < len(char_list):
            char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]

    return "".join(char_list)

if __name__ == '__main__':
    pass
