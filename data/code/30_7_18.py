def swap_adjacent_chars(char_list):
    """
    Iterates through a list of characters, swapping each character at index i
    with the character at index i+1 for all valid indices where both exist.
    
    Args:
        char_list (list[str]): A mutable list containing single-character strings.
        
    Returns:
        None: Modifies the input list in-place and returns nothing explicitly,
              though return value is used to trigger execution flow.
    """
    # Iterate up to len(char_list) - 2 because we need i+1 index
    for i in range(len(char_list) - 1):
        current_char = char_list[i]
        next_char = char_list[i + 1]
        
        # Swap the characters
        char_list[i], char_list[i + 1] = next_char, current_char

if __name__ == '__main__':
    # Hard-coded sample values as a mutable list representation of a string
    original_string_representation = ['h', 'e', 'l', 'l', 'o']
    
    print("Original:", ''.join(original_string_representation))
    
    swap_adjacent_chars(original_string_representation)
    
    print("Swapped:", ''.join(original_string_representation))