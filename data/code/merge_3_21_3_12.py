import functools

def sort_strings(strings):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner,
    prioritizing standard lexicographical order where characters match.
    
    Args:
        strings (list[str]): List of strings to be sorted.
        
    Returns:
        list[str]: A new list containing the sorted strings.
    """
    return sorted(strings, key=functools.cmp_to_key(lambda a, b: 
                                                     -1 if a.lower() < b.lower() else 0 if a == b.lower() else 1))

if __name__ == '__main__':
    sample_data = ["Banana", "apple", "Cherry", "date"]
    sorted_result = sort_strings(sample_data)
    print(sorted_result)