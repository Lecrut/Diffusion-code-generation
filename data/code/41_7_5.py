def to_title_case(strings):
    """
    Converts every string in the input list to title case.
    
    Args:
        strings (list of str): The list of strings to convert.
        
    Returns:
        list of str: A new list with each string converted to title case.
    """
    return [s.title() for s in strings]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    input_list = ["hello", "WORLD", "python", "is!", "awesome"]
    
    result_list = to_title_case(input_list)
    
    print("Input:", input_list)
    print("Output:", result_list)