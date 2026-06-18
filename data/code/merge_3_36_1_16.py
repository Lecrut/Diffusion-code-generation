def reverse_string(text: str) -> str:
    """
    Reverses a given string using slicing notation.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or files
    samples = [
        "Hello, World!",
        "",
        "a",
        "Racecar",
        "Python is great!"
    ]

    print("Input\t->\tReversed")
    print("-" * 40)
    
    for sample in samples:
        result = reverse_string(sample)
        # Use repr to handle special characters safely if needed, but default str join usually suffices
        print(repr(f"{sample}\n{result}"))