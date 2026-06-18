def reverse_string_in_place(s: str) -> str:
    """
    Reverses a string by converting it to a list of characters, 
    reversing in place using two pointers, and joining back into a string.
    
    This approach minimizes memory usage relative to creating new strings 
    at each step (like slicing s[::-1]) because the underlying character 
    array is modified directly before reconstructing the final string only once.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string that is the reverse of the input.
    """
    # Convert string to list for mutability as strings are immutable in Python
    char_list = list(s)
    
    left, right = 0, len(char_list) - 1
    
    # Two-pointer swap approach to minimize operations and memory overhead
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
        
    return "".join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files
    test_cases = [
        "hello",
        "",
        "a",
        "Python Programming",
        "Race a car"
    ]
    
    for text in test_cases:
        reversed_text = reverse_string_in_place(text)
        print(f"Original: {text}")
        print(f"Reversed:{reversed_text}\n")