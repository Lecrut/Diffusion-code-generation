def sort_strings(strings):
    """
    Sorts a list of strings alphabetically (lexicographically).
    Prioritizes standard case-sensitive sorting as per typical requirements,
    though Python's default is ASCII-based uppercase before lowercase which may not be 
    what users expect for 'case-insensitivity'. If strict alphabetical ignoring case is needed:
        return sorted(strings, key=str.lower)
    
    Here we use the raw sort (lexicographical/unicode codepoint order).

    Args:
        strings (list[str]): List of input strings.

    Returns:
        list[str]: New sorted list of strings in ascending lexicographical order.
    """
    return sorted(strings)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or files
    sample_data = ["Banana", "apple", "Cherry", "date"]
    result = sort_strings(sample_data)
    
    print("Sorted list:")
    for item in result:
        print(item)