def sort_strings(strings):
    """Sorts a list of strings alphabetically (lexicographically).
    
    Args:
        strings: A list of strings to be sorted.
        
    Returns:
        The same list with elements reordered in ascending order.
    """
    return sorted(strings)

if __name__ == '__main__':
    sample_data = ["banana", "Apple", "cherry", "apple", "Date"]
    result = sort_strings(sample_data)
    print(result)