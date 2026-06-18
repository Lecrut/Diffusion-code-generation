def calculate_string_length(input_text: str) -> int:
    """
    Calculates the total character length of a given string, 
    including all spaces and punctuation marks.
    
    Parameters:
        input_text (str): The string to be evaluated.
        
    Returns:
        int: The count of characters in the provided string.
    """
    if not isinstance(input_text, str):
        raise TypeError("Input must be a string.")
    return len(input_text)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no interactive input is required
    sample_input = "Hello World! This is a test string."

    result = calculate_string_length(sample_input)
    
    print(f"String: '{sample_input}'")
    print(f"Total character length (including spaces and punctuation): {result}")