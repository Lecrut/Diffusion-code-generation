def reverse_string(s: str) -> str:
    """
    Reverses a string iteratively without using built-in reversal methods.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    # Convert the string to a list of characters since strings are immutable in Python
    char_list = list(s)
    left_index, right_index = 0, len(char_list) - 1
    
    # Iterate until pointers meet or cross each other
    while left_index < right_index:
        # Swap elements at current indices
        temp_char = char_list[left_index]
        char_list[left_index] = char_list[right_index]
        char_list[right_index] = temp_char
        
        # Move pointers towards the center
        left_index += 1
        right_index -= 1
    
    # Join the list back into a string and return it
    return "".join(char_list)

if __name__ == '__main__':
    sample_string = "Hello, World!"
    reversed_string = reverse_string(sample_string)
    
    print(f"Original: {sample_string}")
    print(f"Reversed: {reversed_string}")