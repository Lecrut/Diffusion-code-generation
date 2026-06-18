def reverse_string(s: str) -> str:
    """
    Reverses a string iteratively without using built-in reversal methods.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    # Convert the string to a list since strings are immutable in Python
    char_list = list(s)
    
    left, right = 0, len(char_list) - 1
    
    # Iterate while pointers move towards each other
    while left < right:
        # Swap characters at current pointers
        temp = char_list[left]
        char_list[left] = char_list[right]
        char_list[right] = temp
        
        # Move the inner pointer to next position of outer one
        left += 1
        right -= 1
    
    # Join list into a new string and return it
    reversed_s = "".join(char_list)
    
    return reversed_s

if __name__ == '__main__':
    sample_input = "Hello, World!"
    result = reverse_string(sample_input)
    print(f"Original: {sample_input}")
    print(f"Reversed: {result}")