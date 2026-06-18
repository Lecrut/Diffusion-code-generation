def sort_strings_case_insensitive(strings):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner.
    
    Args:
        strings (list[str]): List of input strings to be sorted.
        
    Returns:
        list[str]: A new list containing the sorted strings. The original 
                  order is preserved as this function does not modify the input.
    """
    # Use the key parameter with str.lower() for case-insensitive sorting comparison
    return [s for s in sorted(strings, key=str.lower)]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or command-line arguments are needed
    sample_data = ["Banana", "apple", "Cherry", "date", "Elderberry"]

    print("Input list:", sample_data)

    sorted_result = sort_strings_case_insensitive(sample_data)

    print("Sorted list (case-insensitive):")
    for item in sorted_result:
        print(item)