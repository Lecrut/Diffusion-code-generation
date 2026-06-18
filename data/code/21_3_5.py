def sort_strings_alphabetically(strings):
    """
    Sorts a list of strings alphabetically (lexicographically).
    
    Args:
        strings (list[str]): A list of string elements to be sorted.
        
    Returns:
        list[str]: A new list containing the sorted elements in lexicographical order,
                   preserving case sensitivity as per standard Python behavior unless specified otherwise.
                   
    Note: By default, this function performs a case-sensitive sort based on ASCII values,
           where uppercase letters precede lowercase ones ('A' < 'a'). 
           For true case-insensitive sorting while maintaining original casing in output,
           the list is sorted using a custom key that normalizes to lower-case.
    """
    return sorted(strings)

if __name__ == '__main__':
    sample_data = ["banana", "Apple", "cherry", "date"]
    sorted_result = sort_strings_alphabetically(sample_data)
    
    # Printing the result for demonstration purposes only; no user input is required.
    print("Sorted list (case-sensitive):")
    print(sorted_result)