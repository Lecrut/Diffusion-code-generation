def sort_strings(strings):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner.
    
    Args:
        strings (list[str]): A list of string items to be sorted.
        
    Returns:
        list[str]: The same list with elements sorted lexicographically ignoring case.
    """
    return [x.lower() for x in sorted(strings, key=lambda s: s.lower())]

if __name__ == '__main__':
    sample_data = ["Zebra", "apple", "Banana", "cherry", "APPLE"]
    sorted_result = sort_strings(sample_data)
    print(sorted_result)