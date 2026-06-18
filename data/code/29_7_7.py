def reverse_string_min_memory(s: str) -> str:
    """
    Reverses a string using minimal memory by converting to a list of characters,
    swapping in place, and joining back into a string. This avoids creating multiple
    intermediate large-string copies that would occur with simple slicing or concatenation loops.

    Args:
        s (str): The input string to reverse.

    Returns:
        str: The reversed string.
    
    Memory Efficiency Note:
        While converting the entire string to a list of characters does create an intermediate copy,
        it is generally more memory-efficient than repeatedly creating new strings during character-by-character 
        construction or slicing loops in certain Python implementations, especially for very large inputs,
        because lists handle resizing differently and avoid full-string duplication at each step.
    """
    # Convert string to list of characters (O(n) space, but single pass access is efficient)
    char_list = list(s)
    
    # Swap elements in place from both ends towards the center (O(1) extra space beyond conversion)
    left_index = 0
    right_index = len(char_list) - 1
    
    while left_index < right_index:
        # Store character at left index
        temp_char = char_list[left_index]
        
        # Assign character from right to left
        char_list[left_index] = char_list[right_index]
        
        # Update the temporary variable with the swapped value
        char_list[right_index] = temp_char
        
        # Move indices towards center
        left_index += 1
        right_index -= 1
    
    # Join list back into a single string (O(n) space for result, unavoidable return type requirement)
    reversed_string = "".join(char_list)
    
    return reversed_string

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    test_cases = [
        "hello",           # Simple case
        "",                # Empty string edge case
        "a"                # Single character edge case
    ]

    for test_input in test_cases:
        reversed_output = reverse_string_min_memory(test_input)
        print(f"Input: '{test_input}' -> Output: '{reversed_output}'")