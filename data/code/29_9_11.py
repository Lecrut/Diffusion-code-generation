def reverse_string(s: str) -> str:
    """
    Reverses a given string using Python's slicing capability.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [
        "hello",
        "Python programming is fun!",
        "",
        "a" * 100,
        "Reverse this string immediately!"
    ]

    print("Input String | Reversed Output")
    print("-" * 45)
    
    for test_input in test_cases:
        reversed_output = reverse_string(test_input)
        # Truncate long output strings to fit the table nicely, max length is set based on input string display needs
        if len(reversed_output) > 30:
            print(f"{test_input!r:<25} | {reversed_output[:30] + '..'}")
        else:
            print(f"{test_input!r:<41} | {reversed_output}")

    # Demonstrate usage with a specific example in the output description if needed, 
    # though not strictly required given the table above.