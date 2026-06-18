def reverse_string(s):
    """
    Reverses a given input string using Python's efficient slicing method.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    test_strings = [
        "Hello, World!",
        "Python is awesome.",
        "",
        "A"
    ]
    
    print("Input strings and their reverses:")
    print("-" * 30)
    for original in test_strings:
        reversed_str = reverse_string(original)
        print(f"Original: '{original}'")
        print(f"Reversed: {reversed_str}\n")