def reverse_string(text: str) -> str:
    """
    Reverses the input string using slicing notation for efficiency.
    
    Args:
        text (str): The string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input or external dependencies
    samples = ["Hello, World!", "Python", "", "A"]

    print("Testing reverse_string function:\n")
    for sample in samples:
        result = reverse_string(sample)
        print(f"Original: '{sample}' -> Reversed: '{result}'")