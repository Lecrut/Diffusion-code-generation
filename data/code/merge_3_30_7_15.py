def swap_adjacent_chars(s_list):
    """
    Iterates through a list of characters representing a string 
    and swaps each character at index i with the character at index i+1,
    provided that both indices are within bounds.
    
    Parameters:
        s_list (list[str]): A mutable list containing single-character strings.
        
    Returns:
        None: Modifies the input list in-place.
    """
    length = len(s_list)
    for i in range(length - 1):
        # Swap character at index i with character at index i+1
        s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]

if __name__ == '__main__':
    sample_string = "hello"
    
    # Convert string to a mutable list of characters for efficiency
    char_list = list(sample_string)
    
    print("Original:", "".join(char_list))
    
    swap_adjacent_chars(char_list)
    
    print("Swapped:", "".join(char_list))