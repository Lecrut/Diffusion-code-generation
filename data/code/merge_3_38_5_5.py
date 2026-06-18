def find_duplicate_chars(s: str) -> set:
    """
    Finds all duplicate characters in a string with O(n) time complexity.
    
    Args:
        s (str): The input string to analyze.
        
    Returns:
        set: A set of unique characters that appear more than once in the string.
    """
    char_count = {}
    duplicates = set()

    for char in s:
        if char in char_count:
            # If we've seen this character before, add it to our results only 
            # when its count exceeds 1 (to avoid adding duplicates of the duplicate itself)
            if char not in duplicates and len(char_count[char]) > 0:
                duplicates.add(char)
        else:
            char_count[char] = 1

    return duplicates

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, etc.)
    test_string_1 = "hello world"
    test_string_2 = "aabbccddaa"
    
    result_1 = find_duplicate_chars(test_string_1)
    result_2 = find_duplicate_chars(test_string_2)

    print(f"Duplicates in '{test_string_1}': {sorted(result_1)}")
    print(f"Duplicates in '{test_string_2}': {sorted(result_2)}")