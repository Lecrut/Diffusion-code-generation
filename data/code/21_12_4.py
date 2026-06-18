import re

def case_insensitive_sort(strings):
    """
    Sorts a list of strings lexicographically in a case-insensitive manner.
    
    Args:
        strings (list[str]): A list of input string elements to sort.
        
    Returns:
        list[str]: The sorted list as per the rules.
    """
    # Create tuples for comparison key, using lowercased version and original index 
    # to maintain stability if keys are equal.
    indexed_strings = [(s.lower(), i) for i, s in enumerate(strings)]
    
    # Sort based on the first element (lowercase string), which ensures case-insensitivity.
    sorted_indexed = sorted(indexed_strings, key=lambda x: x[0])
    
    # Reconstruct the list using original strings from the stable sort results.
    return [s for _, s in sorted_indexed]

if __name__ == '__main__':
    sample_data = ["Banana", "apple", "CHERRY", "date", "Elderberry"]
    print(f"Original List: {sample_data}")
    
    # Sort the list using case-insensitive logic.
    sorted_list = case_insensitive_sort(sample_data)
    
    # Print result clearly as requested, joined with spaces for clarity in a single line per item conceptually 
    # but maintaining readability of the sequence.
    print("Sorted List:")
    for i, val in enumerate(sorted_list):
        print(f"{i + 1}. {val}")