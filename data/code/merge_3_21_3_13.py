def sort_strings(strings):
    """
    Sorts a list of strings alphabetically (lexicographically).
    
    Args:
        strings (list[str]): A list of string elements to be sorted.
        
    Returns:
        list[str]: A new list containing the same strings, sorted in ascending order.
    """
    return sorted(strings)

if __name__ == '__main__':
    sample_data = ["banana", "Apple", "cherry", "date"]
    result = sort_strings(sample_data)
    print(result)