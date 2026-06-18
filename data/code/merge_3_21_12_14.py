def sort_strings_case_insensitive(string_list):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner.
    
    Args:
        string_list (list[str]): A list of strings to be sorted.
        
    Returns:
        list[str]: The same list with elements reordered based on 
                   lexicographical order ignoring case differences.
    """
    # Create a copy of the original list to avoid modifying it in place,
    # though sorting usually modifies the object passed if mutable reference is used.
    sorted_list = string_list.copy()
    
    # Sort using a key that converts each string to lowercase for comparison purposes.
    # This ensures 'Apple' comes before 'banana', and 'Banana' follows 'apple'.
    sorted_list.sort(key=str.lower)
    
    return sorted_list

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files).
    sample_strings = ["Python", "java", "JavaScript", "python3", "JAVASCRIPT"]
    
    print("Original list:")
    for s in sample_strings:
        print(f"  '{s}'")
        
    sorted_result = sort_strings_case_insensitive(sample_strings)
    
    print("\nSorted list (case-insensitive):")
    for s in sorted_result:
        print(f"  '{s}'")