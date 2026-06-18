def reverse_string(s: str) -> str:
    """
    Reverses a given string using slicing notation for maximum efficiency.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed version of the input string.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or file access
    test_cases = [
        "hello",
        "",
        "a" * 100,
        "Python is awesome!"
    ]

    results = []
    print("Input String")
    print("-" * 20)
    
    for test_input in test_cases:
        reversed_output = reverse_string(test_input)
        print(f"'{test_input}' -> '{reversed_output}'")