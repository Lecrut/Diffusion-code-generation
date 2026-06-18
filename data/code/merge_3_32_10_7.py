def calculate_string_length(input_text):
    """
    Calculates the total character length of a given string, 
    including all spaces, punctuation, and special characters.
    
    Parameters:
        input_text (str): The string to measure.
        
    Returns:
        int: The length of the string in characters.
    """
    return len(input_text)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = [
        "Hello, World!",
        "",
        "123 456",
        "\n\t"
    ]

    print("String Length Calculator")
    print("-" * 20)

    for i in range(len(samples)):
        test_string = samples[i]
        length_value = calculate_string_length(test_string)
        
        if len(test_string) > 40: # Prevent printing excessively long strings on a single line
            display_str = test_string[:37] + "..."
        else:
            display_str = test_string
            
        print(f"Sample {i+1}: '{display_str}'")
        print(f"Character count: {length_value}")