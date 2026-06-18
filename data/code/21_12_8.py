def sort_strings_case_insensitive(string_list):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner.
    
    Args:
        string_list (list[str]): A list of strings to be sorted.
        
    Returns:
        list[str]: The new list with strings sorted lexicographically ignoring case.
    """
    # Create a copy of the original list to avoid modifying it in place if not desired,
    # then sort using a key that converts each string to lowercase for comparison purposes.
    return sorted(string_list, key=str.lower)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or external files).
    sample_data = ["Python", "apple", "Banana", "cherry", "Date"]
    
    print("Original list:", sample_data)
    sorted_list = sort_strings_case_insensitive(sample_data)
    print("Sorted list (case-insensitive):", sorted_list)