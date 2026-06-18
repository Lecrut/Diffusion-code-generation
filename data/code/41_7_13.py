def convert_to_title_case(strings):
    """
    Converts a list of strings to title case (first letter uppercase, rest lowercase).
    
    Args:
        strings (list[str]): List of input strings.
        
    Returns:
        list[str]: New list with each string converted to title case.
    """
    return [s.title() for s in strings]

if __name__ == '__main__':
    # Hard-coded sample values; no user input or external dependencies required
    sample_input = ["hello world", "PYTHON IS FUN", "  this is a test  ", "" , "mixed CASE"]
    
    result = convert_to_title_case(sample_input)
    
    print("Input:", sample_input)
    print("Output:", result)