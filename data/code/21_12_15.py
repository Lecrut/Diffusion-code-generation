def sort_strings_case_insensitive(string_list):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner.
    
    Parameters:
        string_list (list[str]): List of input strings to be sorted.
        
    Returns:
        list[str]: A new list with the same elements, but sorted by their lowercase representation.
    """
    # Create a copy of the original list to avoid modifying it in place if not needed elsewhere later
    result = string_list.copy()
    
    # Sort using key=str.lower for case-insensitivity
    result.sort(key=lambda x: x.lower())
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values containing various cases to demonstrate functionality
    input_strings = ["Apple", "banana", "Cherry", "date", "FIGURE"]

    print("Input List:", input_strings)
    
    sorted_list = sort_strings_case_insensitive(input_strings)
    
    print("\nSorted Output:")
    for item in sorted_list:
        # Ensure consistent spacing and clear output even if list items are not uniform length
        print(item.ljust(15), end=' ')
        
    # Also provide a simple Pythonic representation line at the very end of sorting results to complete display clearly
    print(f"\nPython List Representation: {sorted_list}")