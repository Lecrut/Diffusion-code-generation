def reverse_string_iterative(s: str) -> str:
    """
    Reverses a string iteratively without using built-in reversal methods.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
        
    Time Complexity: O(n), where n is the length of the string.
    Space Complexity: O(1) excluding the space required for the output string.
    """
    # Convert the string to a list since strings are immutable in Python
    char_list = list(s)
    
    # Use two pointers approach to swap characters from both ends moving towards center
    left, right = 0, len(char_list) - 1
    
    while left < right:
        # Swap elements at current left and right indices
        temp = char_list[left]
        char_list[left] = char_list[right]
        char_list[right] = temp
        
        # Move pointers towards center
        left += 1
        right -= 1
    
    # Join the list back into a string
    return ''.join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    test_cases = [
        "hello",
        "Python programming is fun!",
        "",
        "a",
        "12345"
    ]

    for original in test_cases:
        reversed_str = reverse_string_iterative(original)
        print(f"Original: '{original}'")
        print(f"Reversed: '{reversed_str}'\n")