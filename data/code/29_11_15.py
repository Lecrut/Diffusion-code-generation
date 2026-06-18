def reverse_word(text: str) -> str:
    """
    Reverses a single string using slicing for maximum efficiency.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: The reversed version of the input string.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = [
        "hello",
        "Python programming is fun!",
        "",
        "a",
        "racecar"
    ]

    print("Input -> Output")
    print("-" * 30)
    
    for sample in samples:
        result = reverse_word(sample)
        print(f"{sample!r} -> {result!r}")