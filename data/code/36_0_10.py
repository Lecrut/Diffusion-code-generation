def reverse_string(input_str):
    """
    Reverses the order of characters in a given string.
    
    Args:
        input_str (str): The string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    test_cases = [
        "Hello, World!",
        "Python Programming",
        "",
        "a"
    ]
    
    for test_input in test_cases:
        reversed_result = reverse_string(test_input)
        print(f"Original: '{test_input}'")
        print(f"Reversed: '{reversed_result}'\n")