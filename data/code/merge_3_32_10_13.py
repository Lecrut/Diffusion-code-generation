def calculate_string_length(s: str) -> int:
    """
    Calculates the total character length of a string, including spaces and punctuation.
    
    Args:
        s (str): The input string to measure.
        
    Returns:
        int: The number of characters in the string.
    """
    return len(s)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user interaction or external inputs)
    sample_input = "Hello, World! This is a test case."
    
    result_length = calculate_string_length(sample_input)
    
    print(f"Input string: '{sample_input}'")
    print(f"Total character length: {result_length}")