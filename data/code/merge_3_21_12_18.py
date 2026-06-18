def sort_strings_case_insensitive(strings):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner.
    
    Args:
        strings (list[str]): A list containing string elements to be sorted.
        
    Returns:
        list[str]: A new list with the same elements, sorted by lowercase value.
    """
    return sorted(strings, key=str.lower)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or arguments)
    sample_data = ["Banana", "apple", "Cherry", "date", "APRICOT"]
    
    print("Original list:")
    for item in sample_data:
        print(f"  - {item}")
        
    sorted_list = sort_strings_case_insensitive(sample_data)
    
    print("\nSorted list (case-insensitive):")
    for item in sorted_list:
        print(f"  - {item}")