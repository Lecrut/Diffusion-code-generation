def reverse_string(s: str) -> str:
    """
    Returns the reversed version of the input string efficiently.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string containing characters from 's' in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = [
        "hello world",
        "",
        "a" * 1000,  # Test with a large string to ensure efficiency
        "Python is awesome!",
        "1234567890"
    ]

    for sample in samples:
        reversed_str = reverse_string(sample)
        print(f"Original: {sample!r}")
        print(f"Reversed: {reversed_str!r}\n")