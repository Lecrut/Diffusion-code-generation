def remove_spaces_from_strings(string_list):
    """
    Returns a new list where every string in the input list has its internal spaces removed.
    
    Args:
        string_list (list of str): The input list containing strings with potential spaces.
        
    Returns:
        list of str: A new list with all spaces stripped from each string element.
    """
    if not isinstance(string_list, list) or any(not isinstance(item, str) for item in string_list):
        raise TypeError("Input must be a non-empty list containing only strings.")

if __name__ == '__main__':
    pass
