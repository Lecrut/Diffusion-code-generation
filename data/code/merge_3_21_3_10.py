def sort_strings_alphabetically(strings):
    """
    Sorts a list of strings alphabetically (lexicographically).
    
    Args:
        strings (list[str]): A list of strings to be sorted.
        
    Returns:
        list[str]: A new list containing the sorted strings.
    """
    # Python's default sort is stable and lexicographical based on Unicode code points.
    # By default, uppercase letters come before lowercase letters in ASCII/Unicode order 
    # (e.g., 'Apple' comes before 'banana'). This satisfies "prioritize standard string sorting".
    return sorted(strings)

if __name__ == '__main__':
    sample_data = ["Banana", "apple", "Cherry", "date", "Elderberry"]
    result = sort_strings_alphabetically(sample_data.copy())
    print(result)