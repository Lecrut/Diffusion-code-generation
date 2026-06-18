def reverse_string(s: str) -> str:
    """
    Reverses a string iteratively without using built-in reversal methods.
    
    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(1) excluding input and output storage if modifying in place, 
                       or O(n) for creating new list/string elements as strings are immutable.
    
    Args:
        s (str): The input string to reverse.
        
    Returns:
        str: The reversed string.
    """
    # Convert the string to a list since strings are immutable in Python
    char_list = list(s)
    
    # Use two pointers approach for iterative reversal
    left, right = 0, len(char_list) - 1
    
    while left < right:
        # Swap characters at current positions of left and right pointer
        temp_char = char_list[left]
        char_list[left] = char_list[right]
        char_list[right] = temp_char
        
        # Move pointers towards the center
        left += 1
        right -= 1
    
    # Join list back to form the reversed string
    return ''.join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    test_cases = [
        "hello world",
        "python programming",
        "",
        "a"
    ]

    for test_input in test_cases:
        reversed_result = reverse_string(test_input)
        print(f'Original: "{test_input}"')
        print(f'Reversed: "{reversed_result}"\n')