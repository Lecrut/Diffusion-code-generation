def swap_adjacent_chars(char_list):
    """
    Iterates through a list of characters, swapping each character at index i
    with the character at index i+1 for all valid indices where both exist.
    
    Args:
        char_list (list[str]): A mutable list containing single-character strings.
        
    Returns:
        None: The input list is modified in place.
    """
    # Iterate up to len(char_list) - 2 because we access i+1 as well
    for i in range(len(char_list) - 2):
        char_at_i = char_list[i]
        char_at_next = char_list[i + 1]
        
        # Swap the characters
        char_list[i] = char_at_next
        char_list[i + 1] = char_at_i

if __name__ == '__main__':
    # Hard-coded sample values as a list of single-character strings representing "hello world"
    original_string_repr = ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]
    
    print("Original:", "".join(original_string_repr))
    
    swap_adjacent_chars(original_string_repr)
    
    print("Modified:", "".join(original_string_repr))