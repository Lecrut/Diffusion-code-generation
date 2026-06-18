def swap_adjacent_chars(char_list):
    """
    Iterates through a list of characters, swapping each character at index i 
    with the character at index i+1 if both indices exist within the list bounds.
    
    Args:
        char_list (list[str]): A mutable list containing single-character strings.
        
    Returns:
        None: Modifies the input list in-place and returns it for convenience.
    """
    n = len(char_list)
    # Iterate up to n-1 because we access i+1, so the last valid index is n-2 when swapping with n-1
    for i in range(n - 1):
        char_at_i = char_list[i]
        char_at_next = char_list[i + 1]
        
        # Perform swap
        char_list[i], char_list[i + 1] = char_at_next, char_at_i

if __name__ == '__main__':
    sample_string = "hello"
    
    # Convert string to a list of characters for mutability
    chars = [c for c in sample_string]
    
    print("Original:", "".join(chars))
    
    swap_adjacent_chars(chars)
    
    print("Swapped:", "".join(chars))