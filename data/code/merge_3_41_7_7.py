def to_title_case(strings):
    """
    Converts a list of strings into title case.
    
    Args:
        strings (list[str]): A list of input strings.
        
    Returns:
        list[str]: A new list with each string converted to title case.
    """
    return [s.title() for s in strings]

if __name__ == '__main__':
    sample_input = ["hello world", "this is a test", "python programming"]
    result = to_title_case(sample_input)
    print(result)