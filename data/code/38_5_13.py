def find_duplicate_characters(s: str) -> list[str]:
    """
    Finds all duplicate characters in a string.
    
    A character is considered duplicated if it appears more than once in the string.
    The function returns a sorted list of unique characters that appear multiple times.
    
    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(1) (since the alphabet size is constant for ASCII/Unicode).

    Args:
        s (str): The input string to analyze.

    Returns:
        list[str]: A sorted list of unique characters that are duplicated in the string.
                   If no duplicates exist, returns an empty list.
    
    Example:
        >>> find_duplicate_characters("aabbcc")
        ['a', 'b', 'c']
        
        >>> find_duplicate_characters("abcde")
        []
        
        >>> find_duplicate_characters("aabbcdd")
        ['a', 'b', 'd']
    """
    char_count = {}

    # First pass: Count the frequency of each character.
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    duplicates = []

    # Second pass: Identify characters with a count greater than 1 and add to list.
    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)

    return sorted(duplicates)

if __name__ == '__main__':
    sample_strings = [
        "aabbcc",           # Expected: ['a', 'b', 'c']
        "hello world!",     # Expected: ['l', 'o'] (ignoring case sensitivity unless specified, here treating as is) 
                           # Note: 'h' appears once, 'e' once, 'w' once, 'd' once. 'l':2, 'o':1? Wait, "hello" -> h,e,l,l,o; "world!" -> w,o,r,l,d,!
                           # Let's trace manually for "hello world!": 
                           # h:1, e:1, l:3 (indices 2,3 and in word), o:1, _:0? No space is char. Space appears once. ! appears once. r:1, d:1.
                           # Actually 'l' appears at index 2 ('h','e'), 3 ('l'), then after space... h,e,l,l,o,w,r,l,d,! -> l is at 2 and 7? 
                           # String: "hello world!"
                           # Indices: 0:h, 1:e, 2:l, 3:l, 4:o, 5: , 6:w, 7:r, 8:l, 9:d, 10:!
                           # Counts: l->3 (idx 2,3,8). Others once. So expected ['l']. 
        "aabbcdd",          # Expected: ['a', 'b', 'd']
        "",                 # Expected: []
        "aaaa"              # Expected: ['a']
    ]

    for test_str in sample_strings:
        result = find_duplicate_characters(test_str)
        print(f"Input: '{test_str}'")
        print(f"Duplicates found: {result}")
        
        if len(result) == 0 and not any(c != '' for c in test_str): # Basic check, though empty string handled correctly by logic.
            pass 
        
        print("-" * 20)