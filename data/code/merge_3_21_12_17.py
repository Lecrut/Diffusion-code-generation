def sort_strings_case_insensitive(strings):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner.
    
    Args:
        strings (list[str]): A list of string elements to be sorted.
        
    Returns:
        list[str]: A new list containing the same strings, sorted lexicographically 
                   ignoring case differences. The original order is preserved for equal items 
                   as per Python's stable sort behavior based on lowercase comparison logic.
    """
    # Create a copy of the input list to avoid modifying the original if necessary,
    # though sorting in-place is also acceptable depending on requirements. Here we return sorted directly.
    return sorted(strings, key=str.lower)

if __name__ == '__main__':
    # Hard-coded sample values as per task constraints (no user input required).
    sample_list = ["Banana", "apple", "Cherry", "date", "Elderberry"]
    
    print("Original list:", sample_list)
    
    sorted_list = sort_strings_case_insensitive(sample_list)
    
    print("\nSorted list (case-insensitive):")
    for item in sorted_list:
        # Printing each element on a new line for clear output as implied by "printed clearly"
        print(item)