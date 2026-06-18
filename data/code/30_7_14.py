def swap_adjacent_chars(char_list):
    """
    Iterates through a list of characters, swapping adjacent elements at index i 
    with element at index i+1 for all valid indices where both exist.
    
    Args:
        char_list (list): A mutable list containing single-character strings or other objects.
        
    Returns:
        None: Modifies the input list in-place.
    """
    # Iterate up to len(char_list) - 2 because we need i+1 to be a valid index
    for i in range(len(char_list) - 1):
        # Swap characters at current index and next index
        char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]

if __name__ == '__main__':
    # Hard-coded sample values as a list of strings (representing the string)
    original_string_representation = ['h', 'e', 'l', 'l', 'o']
    
    print("Original:", "".join(original_string_representation))
    
    swap_adjacent_chars(original_string_representation)
    
    print("Swapped:", "".join(original_string_representation))