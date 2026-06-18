def calculate_string_length(input_string: str) -> int:
    """
    Calculates the total character length of a given string, including spaces and punctuation.
    
    Args:
        input_string (str): The string to measure.
        
    Returns:
        int: The number of characters in the string.
    """
    return len(input_string)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user interaction or file I/O)
    sample_strings = [
        "Hello, World!",
        "Python 3.12 is awesome.",
        "",
        "   ",
        "!@#$%^&*()"
    ]

    for test_input in sample_strings:
        length_result = calculate_string_length(test_input)
        print(f"Input: '{test_input}' -> Length: {length_result}")