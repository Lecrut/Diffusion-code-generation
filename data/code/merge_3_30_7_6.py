def swap_adjacent_characters(char_list):
    """
    Iterates through a list of characters, swapping each character at index i 
    with the character at index i+1 if both indices exist within the list bounds.
    
    Parameters:
        char_list (list[str]): A mutable list containing single-character strings or chars.
        
    Returns:
        None; modifies the input list in-place to simulate string behavior efficiently.
    """
    # Ensure we have at least one element before starting the loop
    if len(char_list) < 2:
        return

    for i in range(len(char_list) - 1):
        # Swap character at index i with character at index i + 1
        char_at_i = char_list[i]
        char_at_ip1 = char_list[i+1]
        
        # Perform the swap to simulate string mutation efficiently using a list
        char_list[i], char_list[i+1] = char_at_ip1, char_at_i

if __name__ == '__main__':
    # Hard-coded sample values as required; no user input or external access needed.
    original_string_representation = ['h', 'e', 'l', 'l', 'o']
    
    print("Original:", ''.join(original_string_representation))
    
    swap_adjacent_characters(original_string_representation)
    
    print("Modified (after swaps):", ''.join(original_string_representation))