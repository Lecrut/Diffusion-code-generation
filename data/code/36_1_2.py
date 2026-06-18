def reverse_string(text: str) -> str:
    """
    Returns a new string that is the reverse of the input text.
    Uses slicing notation for maximum efficiency as per requirements.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: A new string containing characters in reverse order.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    samples = [
        "Hello, World!",
        "",
        "Python is awesome",
        "A"
    ]

    print("Input -> Output")
    print("-" * 30)
    
    for original in samples:
        reversed_str = reverse_string(original)
        print(f"{original!r} -> {reversed_str!r}")