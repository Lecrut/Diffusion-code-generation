def sort_strings_case_insensitive(string_list):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner.
    
    Parameters:
        string_list (list[str]): The input list of strings to be sorted.
        
    Returns:
        list[str]: A new list containing the same strings, sorted case-insensitively.
    """
    # Create a copy of the original list and sort it using a key that converts each element to lowercase
    return sorted(string_list[:], key=str.lower)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or external dependencies)
    sample_strings = ["Banana", "apple", "Cherry", "date", "Elderberry"]

    print("Original list:", sample_strings)
    
    sorted_result = sort_strings_case_insensitive(sample_strings)
    
    print("Sorted list (case-insensitive):")
    for item in sorted_result:
        print(item)