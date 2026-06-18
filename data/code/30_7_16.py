def swap_adjacent_chars(s_list):
    """
    Iterates through a list representation of characters, swapping 
    each character at index i with the character at index i+1 if both indices are valid.
    
    Args:
        s_list (list[str]): A mutable list containing single-character strings representing the input string.
        
    Returns:
        None: Modifies the list in-place and returns it for convenience.
    """
    n = len(s_list)
    # Iterate up to n-1 because we access i+1, so the last valid index is n-2 when swapping with n-1
    for i in range(n - 1):
        char_at_i = s_list[i]
        char_at_next = s_list[i + 1]
        
        # Swap logic: store current value and assign back to original positions
        s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]

    return s_list

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, stdin, or args)
    sample_string_representation = ['h', 'e', 'l', 'l', 'o']
    
    print("Original:", "".join(sample_string_representation))
    
    swapped_list = swap_adjacent_chars(sample_string_representation)
    
    print("Swapped:", "".join(swapped_list))