def to_title_case(strings):
    """
    Converts every string in the input list to title case.
    
    Args:
        strings (list[str]): A list of strings.
        
    Returns:
        list[str]: A new list with all strings converted to title case.
    """
    return [s.title() for s in strings]

if __name__ == '__main__':
    sample_input = ["hello world", "python programming", "data science"]
    result = to_title_case(sample_input)
    print(result)