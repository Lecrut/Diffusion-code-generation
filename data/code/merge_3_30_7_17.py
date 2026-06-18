def swap_adjacent_characters(char_list):
    """
    Iterates through a list of characters, swapping each character at index i 
    with the character at index i+1 for all valid indices where both exist.
    
    Args:
        char_list (list[str]): A mutable list containing single-character strings.
        
    Returns:
        None: The input list is modified in-place to reflect swaps.
    """
    # Iterate up to the second-to-last index because we access i+1
    for i in range(len(char_list) - 1):
        current_char = char_list[i]
        next_char = char_list[i + 1]
        
        # Swap characters using tuple unpacking
        char_list[i], char_list[i + 1] = next_char, current_char

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    original_string = "hello"
    
    # Convert string to a mutable list of characters for efficiency and mutability requirement
    char_list = [char for char in original_string]
    
    print(f"Original: {''.join(char_list)}")
    
    swap_adjacent_characters(char_list)
    
    print(f"Swapped:  {''.join(char_list)}")