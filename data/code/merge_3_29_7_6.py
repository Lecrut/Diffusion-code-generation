def reverse_string_in_place(s: str) -> str:
    """
    Reverses a string by converting it to a list of characters, 
    swapping elements from both ends towards the center, and joining back into a string.
    
    This approach minimizes memory usage relative to creating new strings or lists 
    because it operates directly on the mutable sequence derived from the input without 
    allocating intermediate large structures beyond what is necessary for mutation.
    
    Args:
        s (str): The input string to reverse.
        
    Returns:
        str: A new string that is the reverse of the input. Note that while Python strings are immutable,
             this function avoids unnecessary deep copies or complex data structure allocations 
             by using a list for in-place-like manipulation before joining.
             
    Example:
        >>> reverse_string_in_place("hello")
        'olleh'
    """
    # Convert string to list of characters (O(n) space, but necessary due to immutability)
    char_list = list(s)
    
    # Two-pointer approach for swapping in-place-like manner
    left_index = 0
    right_index = len(char_list) - 1
    
    while left_index < right_index:
        # Swap characters at current pointers
        temp_char = char_list[left_index]
        char_list[left_index] = char_list[right_index]
        char_list[right_index] = temp_char
        
        # Move pointers towards center
        left_index += 1
        right_index -= 1
    
    # Join list back to string (O(n) space for result, unavoidable in Python without external libraries)
    return ''.join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    samples = [
        "hello",
        "Python Programming",
        "",
        "a" * 100,
        "Reverse this string immediately!"
    ]

    for test_input in samples:
        reversed_result = reverse_string_in_place(test_input)
        print(f"Original: '{test_input}'")
        print(f"Reversed: '{reversed_result}'\n")