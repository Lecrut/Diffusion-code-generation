def convert_string(text: str) -> tuple[str, str, str]:
    """
    Converts a given string to lowercase, uppercase, and title case.
    
    Args:
        text (str): The input string to be converted.
        
    Returns:
        A tuple containing three strings representing the original 
        lowercased, uppercased, and titled versions of the input.
    """
    return text.lower(), text.upper(), text.title()

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    sample_text = "Hello World! This is a TEST string."
    
    lower_result, upper_result, title_result = convert_string(sample_text)
    
    print(f"Lowercase: {lower_result}")
    print(f"Uppercase: {upper_result}")
    print(f"Title Case: {title_result}")