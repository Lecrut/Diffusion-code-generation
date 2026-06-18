def to_title_case(strings):
    """
    Converts every string in the input list to title case.
    
    Args:
        strings (list of str): A list containing one or more strings.
        
    Returns:
        list of str: A new list where each element is its corresponding 
                     original string converted to title case.
    """
    return [s.title() for s in strings]

if __name__ == '__main__':
    sample_strings = ["hello world", "python programming", "this is a test"]
    result = to_title_case(sample_strings)
    print(result)