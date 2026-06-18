def sort_strings_case_insensitive(strings):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner.
    
    Args:
        strings (list[str]): A list of string elements to be sorted.
        
    Returns:
        list[str]: The newly sorted list of strings.
    """
    # Create a copy of the original list to avoid modifying it directly if not needed,
    # though sorting in-place is also acceptable for this task's requirements.
    return sorted(strings, key=str.lower)

if __name__ == '__main__':
    # Hard-coded sample values as per requirement (no user input or files).
    sample_data = ["Banana", "apple", "Cherry", "date", "Elderberry"]

    print("Original list:", sample_data)
    
    sorted_list = sort_strings_case_insensitive(sample_data)
    
    print("\nSorted list (case-insensitive):")
    for item in sorted_list:
        # Using f-string to ensure clear formatting without extra markdown fences outside code block logic.
        print(item)