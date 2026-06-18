def reverse_string(text: str) -> str:
    """
    Reverses a string iteratively without using built-in reversal methods.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    chars = list(text)  # Convert string to list for mutability
    
    left_index = 0
    right_index = len(chars) - 1

    while left_index < right_index:
        temp_char = chars[left_index]
        chars[left_index] = chars[right_index]
        chars[right_index] = temp_char
        
        left_index += 1
        right_index -= 1

    return "".join(chars)

if __name__ == '__main__':
    sample_string = "hello world"
    reversed_result = reverse_string(sample_string)
    
    print(f"Original: '{sample_string}'")
    print(f"Reversed: {reversed_result}")