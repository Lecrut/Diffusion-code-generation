def reverse_string(text: str) -> str:
    """
    Reverses the order of characters in the input string.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return text[::-1]

if __name__ == '__main__':
    sample_inputs = [
        "Hello, World!",
        "Python",
        "",
        "!nos era olleP"
    ]

    for test_input in sample_inputs:
        reversed_output = reverse_string(test_input)
        print(f"Original: '{test_input}'")
        print(f"Reversed: '{reversed_output}'\n")