def sort_strings(strings):
    """
    Sorts a list of strings lexicographically by default, case-insensitively if requested.
    
    Args:
        strings (list[str]): The list of strings to be sorted.
        
    Returns:
        list[str]: A new list containing the sorted strings.
    """
    return sorted(strings)

if __name__ == '__main__':
    sample_strings = ["banana", "Apple", "cherry", "apple"]
    result = sort_strings(sample_strings)
    print(result)