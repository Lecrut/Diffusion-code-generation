import sys

def sort_strings_case_insensitive(string_list):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner.
    
    Args:
        string_list (list[str]): A list containing the strings to be sorted.
        
    Returns:
        list[str]: The newly sorted list of strings.
    """
    # Create a copy of the list to avoid modifying the original input unexpectedly,
    # although sorting in-place is also valid here since we return the result.
    unsorted_list = string_list.copy()
    
    # Sort using Python's default sort with key function set to lowercase conversion.
    # This ensures case-insensitive lexicographical ordering (e.g., 'Apple' comes before 'apple').
    sorted_list = sorted(unsorted_list, key=str.lower)
    
    return sorted_list

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input is required; the program runs autonomously.
    sample_strings = [
        "Banana", 
        "apple", 
        "Cherry", 
        "DATE", 
        "elderberry"
    ]
    
    print("Original List:", sample_strings)
    
    sorted_result = sort_strings_case_insensitive(sample_strings)
    
    print("\nSorted List (Case-Insensitive):")
    for item in sorted_result:
        # Ensure clear output formatting. If items contain newlines, they are printed on separate lines naturally by the loop.
        print(item)