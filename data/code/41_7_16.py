def to_title_case(strings):
    """
    Converts a list of strings into title case.
    
    Args:
        strings (list[str]): A list containing one or more string arguments.
        
    Returns:
        list[str]: A new list where each element is the input string converted 
                   to title case using standard Python rules.
    """
    return [s.title() for s in strings]

if __name__ == '__main__':
    sample_strings = ["hello world", "this is a test"]
    result = to_title_case(sample_strings)
    print(result)