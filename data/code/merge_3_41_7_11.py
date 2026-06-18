def to_title_case(strings):
    """
    Converts every string in the input list to title case.
    
    Args:
        strings (list of str): A list containing zero or more strings.
        
    Returns:
        list of str: A new list with each string converted to title case.
    """
    return [s.title() for s in strings]

if __name__ == '__main__':
    sample_data = ["hello world", "this is a test", "python programming"]
    result = to_title_case(sample_data)
    print(result)