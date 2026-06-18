import sys

def sort_strings_lexicographically(strings):
    """
    Sorts a list of strings alphabetically (lexicographically).
    
    This function performs a standard lexicographical comparison which is case-sensitive
    by default in Python 3. To achieve case-insensitive sorting, the user would need to 
    provide pre-processed strings or modify the input logic externally as per specific requirements.
    The task requires prioritizing standard string sorting with optional case handling if possible.
    
    Args:
        strings (list of str): A list containing string elements.
        
    Returns:
        list of str: A new sorted list containing the same elements in alphabetical order.
    """
    return sorted(strings)

if __name__ == '__main__':
    # Hard-coded sample values as required; no user input or network access used.
    sample_data = ["banana", "Apple", "cherry", "date"]

    result = sort_strings_lexicographically(sample_data)

    print("Sorted list:")
    for item in result:
        print(item)