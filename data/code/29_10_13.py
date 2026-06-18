def reverse_string(input_str: str) -> str:
    """
    Reverses a given input string.
    
    Args:
        input_str (str): The string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    samples = [
        "Hello, World!",
        "Python is awesome.",
        "",
        "A man a plan a canal Panama",
        "!nohtpL"
    ]

    for test_input in samples:
        reversed_result = reverse_string(test_input)
        print(f"Original Input: '{test_input}'")
        print(f"Reversed Output: '{reversed_result}'")
        print("-" * 40)