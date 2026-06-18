def find_duplicate_characters(s: str) -> list[str]:
    """
    Find all duplicate characters in a string.
    
    A character is considered duplicated if it appears more than once in the string.
    The result includes each unique character that has duplicates, listed exactly once per 
    such character (not repeated for every occurrence).
    
    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(k) where k is the number of unique characters in the alphabet used.

    Args:
        s (str): The input string to search for duplicates.

    Returns:
        list[str]: A sorted list of unique characters that appear more than once in the string.
    """
    char_count = {}
    
    # First pass: count frequency of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    duplicates = []
    
    # Second pass: collect characters with count > 1
    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)
    
    return sorted(duplicates)

if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicate_characters(sample_string)
    print(f"Duplicate characters in '{sample_string}': {result}")