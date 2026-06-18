def reverse_string(s: str) -> str:
    """
    Reverses a string iteratively without using built-in reversal methods.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    result = []
    for i in range(len(s) - 1, -1, -1):
        result.append(s[i])
    
    return ''.join(result)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_cases = [
        "hello",
        "Python",
        "",
        "a" * 10,
        "racecar"
    ]

    for text in test_cases:
        reversed_text = reverse_string(text)
        print(f"Original: {text} -> Reversed: {reversed_text}")