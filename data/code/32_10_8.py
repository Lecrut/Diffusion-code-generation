def calculate_total_length(text: str) -> int:
    """
    Calculates the total character length of a string, including spaces 
    and punctuation marks.
    
    Args:
        text (str): The input string to measure.
        
    Returns:
        int: The total number of characters in the string.
    """
    return len(text)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    # No user interaction, command-line arguments, or network access used
    
    samples = [
        "Hello World!",
        "Python is great.",
        "",
        "!@#$%^&*()"
    ]

    for text in samples:
        length = calculate_total_length(text)
        print(f"Input: '{text}'")
        print(f"Total character length: {length}")