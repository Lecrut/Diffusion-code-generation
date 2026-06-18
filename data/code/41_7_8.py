def convert_to_title_case(strings):
    """
    Converts every string in the input list to title case.
    
    Parameters:
        strings (list of str): The list of strings to be converted.
        
    Returns:
        list of str: A new list with all strings converted to title case.
    """
    return [s.title() for s in strings]

if __name__ == '__main__':
    sample_strings = ["hello world", "this is a test", "PYTHON IS FUN"]
    result = convert_to_title_case(sample_strings)
    print(result)