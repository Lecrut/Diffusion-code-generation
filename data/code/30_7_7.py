def swap_adjacent_characters(s_list):
    """
    Iterates through a list representation of a string and swaps 
    characters at index i with character at index i+1 for all valid i.
    
    Args:
        s_list (list[str]): A mutable list containing single-character strings representing the input string.
        
    Returns:
        None: Modifies the list in-place to perform the swaps.
    """
    n = len(s_list)
    # Iterate up to the second-to-last index because we need i+1
    for i in range(n - 1):
        s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, command-line arguments, or network access is used.
    
    # Sample string converted to a list of characters for mutability efficiency
    original_string = "Hello"
    char_list = list(original_string)
    
    print(f"Original: {''.join(char_list)}")
    
    swap_adjacent_characters(char_list)
    
    print(f"After swapping adjacent pairs (left-to-right): {''.join(char_list)}")