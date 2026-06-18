def calculate_total_length(text: str) -> int:
    """
    Calculates the total character length of a string, 
    including spaces and punctuation marks.
    
    Parameters:
        text (str): The input string to measure.
        
    Returns:
        int: The length of the string in characters.
    """
    return len(text)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or network access
    sample_text = "Hello, World! This is a test."

    result = calculate_total_length(sample_text)

    print(f"Input: '{sample_text}'")
    print(f"Total character length (including spaces and punctuation): {result}")