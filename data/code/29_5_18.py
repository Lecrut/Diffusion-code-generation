def reverse_string_iterative(s: str) -> str:
    """
    Reverses a string iteratively in O(n) time complexity without using built-in reversal methods.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    characters = list(s)  # Convert string to list for mutability
    
    left, right = 0, len(characters) - 1
    
    while left < right:
        # Swap characters at current pointers
        temp = characters[left]
        characters[left] = characters[right]
        characters[right] = temp
        
        left += 1
        right -= 1
    
    return ''.join(characters)

if __name__ == '__main__':
    sample_strings = [
        "hello",
        "Python Programming",
        "",
        "a"
    ]

    for test_input in sample_strings:
        reversed_output = reverse_string_iterative(test_input)
        print(f'Input: "{test_input}" -> Output: "{reversed_output}"')