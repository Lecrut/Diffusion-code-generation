def convert_string(text: str) -> tuple[str, str, str]:
    """
    Converts a given string to lowercase, uppercase, and title case.
    
    Args:
        text (str): The input string to be converted.
        
    Returns:
        A tuple containing three strings: 
            - Lowercase version of the input
            - Uppercase version of the input
            - Title case version of the input
    """
    lowercase_text = text.lower()
    uppercase_text = text.upper()
    title_case_text = text.title()
    
    return (lowercase_text, uppercase_text, title_case_text)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies
    sample_input = "Hello World! This is a TEST string."
    
    lowercase_result, uppercase_result, title_result = convert_string(sample_input)
    
    print("Original:", repr(sample_input))
    print("\nLowercase:")
    print(lowercase_result)
    print("\nUppercase:")
    print(uppercase_result)
    print("\nTitle Case:")
    print(title_result)