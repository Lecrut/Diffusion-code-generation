def find_duplicate_characters(s: str) -> list[str]:
    """
    Find all duplicate characters in a string.
    
    A character is considered duplicated if it appears more than once in the string.
    The function returns a list of unique characters that are duplicates, 
    maintaining their order of first appearance as per standard conventions unless specified otherwise.
    
    Time Complexity: O(n) - Single pass through the string to build frequency map and second pass (or during same pass logic).
    Space Complexity: O(1) in terms of alphabet size (max 26 for lowercase English letters), or O(k) where k is character set size.

    Args:
        s (str): The input string to analyze.

    Returns:
        list[str]: A list of characters that appear more than once in the input string.
    """
    # Dictionary to store frequency of each character
    char_count = {}
    
    # First pass: Count occurrences of all characters
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 0
            
    duplicates_list = []
    
    # Second conceptual step combined with filter logic during first iteration 
    # but to ensure clarity and O(n) single logical flow without multiple full passes over data structures,
    # we can iterate again or use the counts directly. Since dictionary operations are average O(1),
    # iterating through keys is proportional to unique characters which is <= n.
    
    for char in s:  # Iterate over string length 'n' again if needed for order preservation of first appearance, 
                   # OR just iterate over dict.keys() and sort by insertion logic if strict order required.
                   # However, simplest O(n) approach without complex tracking structures is to count then check.
        pass

    # To strictly follow "find all duplicate characters" usually implies returning the set of such chars.
    # Let's refine: iterate through unique keys found in char_count. If count > 1, add to list.
    
    duplicates_set = []
    for char, count in char_count.items():
        if count > 1:
            duplicates_set.append(char)

    return duplicates_set

if __name__ == '__main__':
    # Hard-coded sample values as per requirement (no input(), sys.stdin, etc.)
    test_strings = [
        "hello world",       # h,e,l,o,w,r,d -> l appears twice, o appears twice. Expected: ['l', 'o'] or similar depending on order logic. 
                           # Note: In Python 3.7+, dict preserves insertion order. First seen is 'h','e','l'...
        "aabbcc",            # a,b,c each appear twice.
        "abcdefg",           # No duplicates expected.
        "",                  # Empty string.
    ]

    for test_str in test_strings:
        result = find_duplicate_characters(test_str)
        print(f"Input: '{test_str}'")
        print(f"Duplicates found: {result}")
        
        # Verification logic (optional debug output based on manual trace):
        if not isinstance(result, list):
            raise TypeError("Result must be a list of characters.")