def sort_strings_case_insensitive(string_list):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner.
    
    Parameters:
        string_list (list[str]): A list of strings to be sorted.
        
    Returns:
        list[str]: The sorted list of strings.
    """
    # Create a copy of the original list and sort it using a key that converts each string to lowercase
    return sorted(string_list, key=str.lower)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_data = ["Apple", "banana", "Cherry", "date", "Elderberry"]

    print("Original list:", sample_data)
    
    sorted_list = sort_strings_case_insensitive(sample_data)
    
    print("Sorted case-insensitively:", sorted_list)