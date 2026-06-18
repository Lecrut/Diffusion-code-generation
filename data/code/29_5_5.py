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
    
    # Use two pointers approach for O(n) time complexity
    left_index = 0
    right_index = len(char_list) - 1
    
    while left_index < right_index:
        # Swap the elements at the current indices
        temp_char = char_list[left_index]
        char_list[left_index] = char_list[right_index]
        char_list[right_index] = temp_char
        
        # Move pointers towards the center
        left_index += 1
        right_index -= 1
    
    # Join the list back into a string and return
    return "".join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    test_cases = [
        "hello",
        "Python Programming",
        "",
        "a"
    ]

    for test_input in test_cases:
        reversed_result = reverse_string(test_input)
        print(f"Original: '{test_input}'")
        print(f"Reversed: '{reversed_result}'\n")