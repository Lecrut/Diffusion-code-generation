def reverse_string(text: str) -> str:
    """
    Reverses the order of characters in the input string.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: A new string with characters in reverse order.
    """
    return text[::-1]

if __name__ == '__main__':
    sample_input = "Hello, World!"
    result = reverse_string(sample_input)
    print(result)