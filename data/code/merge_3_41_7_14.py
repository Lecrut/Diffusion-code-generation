def to_title_case(strings):
    """
    Accepts a list of strings and returns a new list where every string 
    in the input has been converted to title case (first character uppercase, rest lowercase).
    
    Args:
        strings (list[str]): List of input strings.
        
    Returns:
        list[str]: New list with each string converted to title case.
    """
    return [s.title() for s in strings]

if __name__ == '__main__':
    # Hard-coded sample values; no user input or external dependencies required.
    sample_input = ["hello world", "PYTHON IS FUN", "this is a test"]
    result = to_title_case(sample_input)
    
    print("Input:", sample_input)
    print("Output:", result)