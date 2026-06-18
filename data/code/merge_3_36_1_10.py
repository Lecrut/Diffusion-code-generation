def reverse_string(text: str) -> str:
    """
    Returns a new string that is the reverse of the input text using slicing notation.
    
    Args:
        text (str): The original string to be reversed.
        
    Returns:
        str: A newly allocated string with characters in reverse order.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    samples = [
        "Hello, World!",
        "",
        "a",
        "Python is awesome.",
        12345 if isinstance(12345, int) else None  # Ensures type hint correctness in docstring context
    ]

    for sample in samples:
        result = reverse_string(sample)
        print(f"Original: {sample!r}")
        print(f"Reversed:{result!r}\n")