def reverse_string(s: str) -> str:
    """
    Returns the reversed version of the input string using slicing notation.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string containing characters in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Sample test cases with hard-coded values, no user interaction required
    samples = [
        "Hello, World!",
        "Python Programming",
        "",
        "a" * 100,
        "!@#$%^&*()_+-=[]{}|;:,.<>?"
    ]

    for sample in samples:
        result = reverse_string(sample)
        print(f"Original: {sample}")
        print(f"Reversed: {result}\n")