def find_duplicate_characters(s: str) -> list[str]:
    """
    Find all duplicate characters in a string.
    
    A character is considered duplicated if it appears more than once in the string.
    The function returns a sorted list of unique characters that appear multiple times.
    
    Args:
        s (str): Input string to analyze
        
    Returns:
        list[str]: Sorted list of duplicate characters as strings
    """
    char_count = {}
    
    # First pass: count frequency of each character in O(n) time
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    duplicates = []
    
    # Second pass: collect characters with count > 1 in O(26) or O(k) time where k is unique chars
    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)
    
    return sorted(duplicates)

if __name__ == '__main__':
    # Hard-coded sample values - no user input required
    test_string = "hello world"
    
    result = find_duplicate_characters(test_string)
    
    print(f"Input string: '{test_string}'")
    print(f"Duplicate characters found: {result}")