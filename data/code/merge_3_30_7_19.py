def swap_adjacent_characters(s_list):
    """
    Iterates through a list representation of a string (or any sequence) 
    and swaps characters at index i with index i+1 for all valid i.
    
    Args:
        s_list (list): A mutable list containing the elements to be processed.
        
    Returns:
        None: Modifies the input list in place.
    """
    # Check if the input is not empty and has at least two elements
    for i in range(len(s_list) - 1):
        # Swap element at current index with next index
        s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, files, or network)
    original_string_representation = ['h', 'e', 'l', 'l', 'o']
    
    print("Original list:", original_string_representation)
    
    swap_adjacent_characters(original_string_representation)
    
    print("Swapped list:", original_string_representation)