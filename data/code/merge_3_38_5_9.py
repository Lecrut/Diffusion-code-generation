def find_duplicates(s: str) -> list[str]:
    """
    Find all duplicate characters in a string.
    
    A character is considered duplicated if it appears more than once in the string.
    The result includes each unique character that has duplicates, listed only once per 
    such character (not repeated for every occurrence).
    
    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(k) where k is the number of unique characters in ASCII/Unicode range used.

    Args:
        s (str): The input string to analyze.

    Returns:
        list[str]: A sorted list of unique duplicate characters found in the string.
    """
    char_count = {}
    
    # Count occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    duplicates = []
    
    # Identify characters that appear more than once
    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)
    
    return sorted(duplicates)

if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(f"Duplicate characters in '{sample_string}': {result}")

# Additional test cases without user input for validation purposes:
test_cases = [
    ("aabbcc", ['a', 'b', 'c']),
    ("abcdef", []),
    ("aaaabbbbccccdddd", ['a', 'b', 'c', 'd']),
    ("Mississippi", ['i', 's', 'p']),  # Note: order depends on sort, here sorted output expected
]

for test_input, expected in test_cases:
    res = find_duplicates(test_input)
    if res == expected:
        print(f"Test passed for '{test_input}'")
    else:
        print(f"Test failed for '{test_input}'. Expected {expected}, got {res}")