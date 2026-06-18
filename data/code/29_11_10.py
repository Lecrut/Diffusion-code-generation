def reverse_word(s: str) -> str:
    """
    Returns a reversed version of the input string using slicing.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string containing characters from 's' in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = [
        "hello",
        "Python programming is fun!",
        "",
        "a",
        "12345"
    ]

    print("Input String | Reversed Output")
    print("-" * 40)
    
    for sample in samples:
        reversed_str = reverse_word(sample)
        print(f"{sample!r}       -> {reversed_str!r}")