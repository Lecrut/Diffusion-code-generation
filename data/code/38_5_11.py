def find_duplicate_characters(s: str) -> list[str]:
    """
    Find all duplicate characters in a string.
    
    A character is considered duplicated if it appears more than once in the string.
    The result contains each unique character that has duplicates, listed exactly once per such character.
    
    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(1) (since the alphabet size is fixed at 26 for lowercase English letters).

    Args:
        s (str): The input string to analyze.

    Returns:
        list[str]: A list of unique characters that appear more than once in the string, 
                  sorted by their first appearance order or simply collected as found.
                  To ensure deterministic output without relying on hash map iteration order,
                  we sort the result alphabetically for consistency unless specified otherwise.
    """
    char_count = {}
    
    # First pass: count occurrences of each character
    for char in s:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    
    duplicates = []
    
    # Second pass: collect characters that appear more than once
    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)
    
    return sorted(duplicates)

if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicate_characters(sample_string)
    print(f"Duplicate characters in '{sample_string}': {result}")

    # Additional test case with uppercase and numbers to ensure robustness
    sample_string2 = "aabbCC123aaBBccDD"
    result2 = find_duplicate_characters(sample_string2)
    print(f"Duplicate characters in '{sample_string2}': {result2}")