import string

def sort_strings_case_insensitive(strings):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner.
    
    Args:
        strings (list[str]): A list of input strings to be sorted.
        
    Returns:
        list[str]: A new list containing the sorted strings.
    """
    # Create a copy of the original list to avoid modifying it in place
    result = strings.copy()
    
    # Sort using a key that converts each string to lowercase for comparison,
    # ensuring case-insensitivity while preserving original casing in output.
    result.sort(key=str.lower)
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed).
    sample_data = ["Banana", "apple", "Cherry", "date", "Elderberry"]

    print("Original list:", sample_data)
    
    sorted_list = sort_strings_case_insensitive(sample_data)
    
    print("Sorted list (case-insensitive):")
    for item in sorted_list:
        print(item)