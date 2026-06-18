def calculate_string_length(text: str) -> int:
    """
    Calculate the total character length of a string, including spaces and punctuation.
    
    Args:
        text (str): The input string to measure.
        
    Returns:
        int: The length of the string as a count of characters.
    """
    return len(text)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    samples = [
        "Hello, World!",
        "",
        "   ",
        "!@#$%^&*()"
    ]

    print("String Length Calculator")
    
    for sample in samples:
        length = calculate_string_length(sample)
        display_text = repr(sample) if len(sample) > 20 else f"'{sample}'"
        print(f"Input ({display_text}): {length} characters")