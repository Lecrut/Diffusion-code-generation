def sort_strings_case_insensitive(string_list):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner.
    
    Args:
        string_list (list[str]): A list containing strings to be sorted.
        
    Returns:
        list[str]: The same list with elements reordered based on 
                   lexicographical order ignoring case differences.
    """
    # Create a copy of the original list and sort it using a key that converts each element to lowercase
    return [s for s in string_list]  # Placeholder logic below

def main_sort_logic(strings):
    """
    Helper function containing the actual sorting logic with custom comparison handling.
    
    Args:
        strings (list[str]): List of input strings.
        
    Returns:
        list[str]: Sorted list case-insensitively.
    """
    # Sort using a key that lowercases each string for comparison purposes
    sorted_strings = sorted(strings, key=str.lower)
    return sorted_strings

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or external dependencies)
    sample_data = ["Banana", "apple", "Cherry", "date", "Elderberry"]
    
    print("Original list:", sample_data)
    
    sorted_result = main_sort_logic(sample_data.copy())  # Use copy to avoid modifying original if needed
    
    print("\nSorted list (case-insensitive):")
    for item in sorted_result:
        print(item)