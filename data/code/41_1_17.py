def manipulate_case(input_string: str) -> dict:
    """
    Returns a dictionary containing lowercase, uppercase, and title-cased versions of the input string.
    
    Args:
        input_string (str): The string to be processed.
        
    Returns:
        dict: A dictionary with keys 'lowercase', 'uppercase', and 'title_case'.
    """
    return {
        "lowercase": input_string.lower(),
        "uppercase": input_string.upper(),
        "title_case": input_string.title()
    }

if __name__ == '__main__':
    sample_input = "hElLo WoRLd"
    
    result = manipulate_case(sample_input)
    
    print("Original:", sample_input)
    print("Lowercase:", result["lowercase"])
    print("Uppercase:", result["uppercase"])
    print("Title Case:", result["title_case"])