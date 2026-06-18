def manipulate_case(input_string: str) -> dict:
    """
    Returns a dictionary containing lowercase, uppercase, and title-cased versions of the input string.
    
    Args:
        input_string (str): The string to be transformed.
        
    Returns:
        dict: A dictionary with keys 'lowercase', 'uppercase', and 'title'.
    """
    return {
        "lowercase": input_string.lower(),
        "uppercase": input_string.upper(),
        "title": input_string.title()
    }

if __name__ == '__main__':
    sample_input = "hElLo WoRLd"
    
    result = manipulate_case(sample_input)
    
    print(f"Input: {sample_input}")
    print(result)