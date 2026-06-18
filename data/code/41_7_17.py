def to_title_case(strings):
    """
    Converts every string in the input list to title case.
    
    Args:
        strings (list of str): A list of strings to be converted.
        
    Returns:
        list of str: A new list with all strings converted to title case.
    """
    return [s.title() for s in strings]

if __name__ == '__main__':
    sample_list = ["hello world", "python is great!", "machine learning"]
    result = to_title_case(sample_list)
    print(result)