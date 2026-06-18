def sort_strings_case_insensitive(string_list):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner.
    
    Args:
        string_list (list[str]): A list containing strings to be sorted.
        
    Returns:
        list[str]: The new sorted list.
    """
    # Create a copy of the original list and sort it using a key that converts 
    # each element to lowercase for case-insensitive comparison.
    return sorted(string_list, key=str.lower)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files).
    sample_data = ["Apple", "banana", "Cherry", "date", "Elderberry"]

    print("Original list:", sample_data)
    
    sorted_list = sort_strings_case_insensitive(sample_data)
    
    print("Sorted list (case-insensitive):")
    for item in sorted_list:
        print(item)