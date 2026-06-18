def convert_to_title_case(strings):
    """
    Converts a list of strings to title case.
    
    Args:
        strings (list[str]): A list containing string elements.
        
    Returns:
        list[str]: A new list with each element converted to title case.
    """
    return [s.title() for s in strings]

if __name__ == '__main__':
    sample_input = ["hello", "WORLD", "python is great"]
    result = convert_to_title_case(sample_input)
    print(result)