def reverse_string(s: str) -> str:
    """
    Returns a new string that is the reverse of the input string.
    
    Args:
        s (str): The original string to be reversed.
        
    Returns:
        str: A new string containing characters from the original in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    samples = [
        "hello",
        "Python programming is fun!",
        "",
        "A man, a plan, a canal: Panama"
    ]

    print("Original String | Reversed String")
    print("-" * 40)
    
    for sample in samples:
        reversed_sample = reverse_string(sample)
        print(f"{sample!r:<35} {reversed_sample!r}")