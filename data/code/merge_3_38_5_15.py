def find_duplicate_characters(s: str) -> list[str]:
    """
    Finds all duplicate characters in a string.
    
    A character is considered duplicated if it appears more than once in the string.
    The function returns a sorted list of unique characters that are duplicates,
    preserving only one instance per repeating character to avoid redundancy 
    (e.g., for 'a' appearing 3 times, it will appear once in the result).

    Time Complexity: O(n) - Single pass through the string.
    Space Complexity: O(1) - Fixed size set of ASCII characters (52 if case-sensitive, less otherwise).

    Args:
        s (str): The input string to analyze.

    Returns:
        list[str]: A sorted list of unique duplicate characters found in the string.
    
    Example:
        >>> find_duplicate_characters("aabbcc")
        ['a', 'b', 'c']
        >>> find_duplicate_characters("hello world!")
        ['l', 'o'] (assuming case-sensitive and ignoring spaces/punctuation unless specified)
    """
    char_count = {}
    
    # First pass: Count occurrences of each character
    for char in s:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    
    duplicates = []
    
    # Second pass: Identify characters with count > 1 and sort them
    for char, count in sorted(char_count.items()):
        if count > 1:
            duplicates.append(char)
            
    return duplicates

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    test_cases = [
        "aabbcc",           # Expected: ['a', 'b', 'c']
        "hello world!",     # Expected: ['l', 'o'] (case-sensitive, space and ! not duplicated)
        "programming",      # Expected: ['r', 'g', 'm'], sorted -> ['g', 'm', 'r']? Let's trace: p(2), r(2), o(1), g(2), a(1), m(1), i(1). Duplicates: p, r, g. Sorted: ['p', 'g' is wrong order], sorted(['p','r','g']) -> ['g', 'p', 'r']
        "aaaa",             # Expected: ['a']
        "",                 # Expected: []
    ]

    for test_input in test_cases:
        result = find_duplicate_characters(test_input)
        print(f"Input: '{test_input}'")
        print(f"Duplicates found: {result}")
        print("-" * 20)