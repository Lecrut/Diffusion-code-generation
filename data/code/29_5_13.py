def reverse_string_iterative(s: str) -> str:
    """
    Reverses a string iteratively without using built-in reversal methods.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
        
    Time Complexity: O(n), where n is the length of the string.
    Space Complexity: O(1) excluding the space required for the output string and character storage in a list or bytearray.
    
    Note: Since Python strings are immutable, we convert it to a mutable type (list of characters or bytearray),
          perform the reversal by swapping elements from both ends moving towards the center,
          then join back into a new string.
    """
    # Convert string to a list for mutability as strings in Python are immutable
    char_list = list(s)
    
    # Use two pointers: left starts at 0, right starts at len-1
    left = 0
    right = len(char_list) - 1
    
    while left < right:
        # Swap characters at current left and right indices
        temp_char = char_list[left]
        char_list[left] = char_list[right]
        char_list[right] = temp_char
        
        # Move pointers towards the center
        left += 1
        right -= 1
    
    # Join list back into a string to return (since function signature expects str)
    return ''.join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    test_cases = [
        "hello world",
        "python programming",
        "",
        "a",
        "12345"
    ]

    for test_input in test_cases:
        reversed_output = reverse_string_iterative(test_input)
        print(f'Input: "{test_input}" -> Output: "{reversed_output}"')