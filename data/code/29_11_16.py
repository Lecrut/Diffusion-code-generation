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
        "Hello, World!",
        "Python Programming",
        "",
        "a"
    ]

    print("Testing reverse_word function:")
    for item in samples:
        result = reverse_word(item)
        print(f'Input: "{item}" -> Output: "{result}"')