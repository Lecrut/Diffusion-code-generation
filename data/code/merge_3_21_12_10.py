def sort_strings_case_insensitive(string_list):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner.
    
    Args:
        string_list (list[str]): A list containing strings to be sorted.
        
    Returns:
        list[str]: The same list with elements reordered based on 
                   lexicographical order ignoring case differences.
    """
    # Create a copy of the original list to avoid modifying it in place
    sorted_strings = string_list.copy()
    
    # Sort using a key that converts each string to lowercase for comparison
    sorted_strings.sort(key=str.lower)
    
    return sorted_strings

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_data = ["Banana", "apple", "Cherry", "date", "Elderberry"]

    print("Original list:")
    for item in sample_data:
        print(f"  - {item}")

    sorted_result = sort_strings_case_insensitive(sample_data)

    print("\nSorted list (case-insensitive):")
    for item in sorted_result:
        print(f"  - {item}")