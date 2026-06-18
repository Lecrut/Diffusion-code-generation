def reverse_string_in_place(s: str) -> str:
    """
    Reverses a string by converting it to a list of characters, 
    swapping elements from both ends towards the center, and joining back into a string.
    
    This approach minimizes memory usage relative to creating new strings or copies 
    because it only creates one intermediate list object (which is necessary in Python 
    since strings are immutable) rather than multiple concatenated slices which create garbage.
    
    Args:
        s (str): The input string to reverse.
        
    Returns:
        str: The reversed string.
    """
    # Convert the string to a list of characters for mutability
    char_list = list(s)
    
    # Two-pointer approach to swap elements in place
    left, right = 0, len(char_list) - 1
    
    while left < right:
        # Swap characters at current pointers
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
        
    # Join the list back into a single string and return it. 
    # This is more efficient than repeated concatenation in loops.
    return ''.join(char_list)

if __name__ == '__main__':
    sample_strings = [
        "hello",
        "Python programming",
        "",
        "a"
    ]

    for test_str in sample_strings:
        reversed_result = reverse_string_in_place(test_str)
        print(f"Original: '{test_str}'")
        print(f"Reversed: '{reversed_result}'\n")