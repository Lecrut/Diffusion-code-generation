def sort_strings_case_insensitive(string_list):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner.
    
    Parameters:
        string_list (list[str]): A list of strings to be sorted.
        
    Returns:
        list[str]: The new sorted list containing the same elements as input, 
                   but ordered based on their lowercase representations.
    """
    return sorted(string_list, key=str.lower)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    sample_data = ["Banana", "apple", "Cherry", "date", "Elderberry"]

    print("Original list:", sample_data)
    
    sorted_list = sort_strings_case_insensitive(sample_data)
    
    print("\nSorted list (case-insensitive):")
    for item in sorted_list:
        print(item)