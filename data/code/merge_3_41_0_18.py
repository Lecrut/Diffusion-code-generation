def transform_string(text: str) -> tuple[str, str, str]:
    """
    Converts a given string to lowercase, uppercase, and title case.
    
    Args:
        text (str): The input string to be transformed.
        
    Returns:
        tuple[str, str, str]: A tuple containing the lowercased, uppercased, 
                              and titled versions of the input string.
    """
    lowercase_result = text.lower()
    uppercase_result = text.upper()
    titlecase_result = text.title()
    
    return lowercase_result, uppercase_result, titlecase_result

if __name__ == '__main__':
    # Hard-coded sample value for testing without user input or CLI arguments
    sample_input = "Hello World! This is a Python Script."
    
    lower_res, upper_res, title_res = transform_string(sample_input)
    
    print(f"Original: {sample_input}")
    print(f"Lowercase: {lower_res}")
    print(f"Uppercase: {upper_res}")
    print(f"Title Case: {title_res}")