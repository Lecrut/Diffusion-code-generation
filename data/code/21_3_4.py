def sort_strings(strings):
    """
    Sorts a list of strings alphabetically (lexicographically).
    
    Args:
        strings (list[str]): A list of string elements to be sorted.
        
    Returns:
        list[str]: The new sorted list.
    """
    return sorted(strings)

if __name__ == '__main__':
    sample_data = ["Banana", "apple", "Cherry", "date"]
    result = sort_strings(sample_data)
    
    print("Sorted strings:")
    for item in result:
        print(item)