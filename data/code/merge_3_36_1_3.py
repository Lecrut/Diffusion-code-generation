def reverse_string(s: str) -> str:
    """
    Returns the reversed version of the input string using slicing notation.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string containing characters from the original string in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [
        "hello",
        "Python programming is fun!",
        "",
        "A"
    ]

    print("Input\tReverse")
    print("-" * 30)
    
    for text in test_cases:
        reversed_text = reverse_string(text)
        print(f"{text}\t{reversed_text}")