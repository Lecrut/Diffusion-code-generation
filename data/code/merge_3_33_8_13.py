def remove_spaces_from_strings(string_list):
    """
    Returns a new list where every string in the input list has its internal spaces removed.
    
    Args:
        string_list (list of str): The list of strings to process.
        
    Returns:
        list of str: A new list with spaces removed from each string.
    """
    return [s.replace(" ", "") for s in string_list]

if __name__ == '__main__':
    sample_data = ["hello world", "python is great", "", "no spaces here"]
    result = remove_spaces_from_strings(sample_data)
    print(result)