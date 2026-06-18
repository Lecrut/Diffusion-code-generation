def calculate_string_length(input_text: str) -> int:
    """
    Calculates the total character length of a given string, including spaces and punctuation.
    
    Args:
        input_text (str): The string to measure
        
    Returns:
        int: Total number of characters in the string
    """
    return len(input_text)

if __name__ == '__main__':
    # Hard-coded sample values for testing, no external user interaction required.
    sample_input = "Hello World!"

    result_length = calculate_string_length(sample_input)

    print(f"Input: '{sample_input}'")
    print(f"Total character length (including spaces and punctuation): {result_length}")