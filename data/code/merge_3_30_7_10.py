def swap_adjacent_chars(characters):
    """
    Iterates through a list of characters, swapping each character at index i 
    with the character at index i+1 for all valid i where 0 <= i < len-1.
    
    Args:
        characters (list[str]): A mutable list containing string characters.
        
    Returns:
        None: Modifies the input list in place and returns it to allow chaining or further use.
    """
    n = len(characters)
    for i in range(n - 1):
        # Swap character at index i with adjacent character at index i+1
        characters[i], characters[i + 1] = characters[i + 1], characters[i]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    original_string_list = ['h', 'e', 'l', 'l', 'o']
    
    print("Original:", ''.join(original_string_list))
    
    swap_adjacent_chars(original_string_list)
    
    print("Swapped:", ''.join(original_string_list))