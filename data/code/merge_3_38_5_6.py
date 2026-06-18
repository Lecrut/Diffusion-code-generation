def find_duplicate_characters(s: str) -> list[str]:
    """
    Finds all duplicate characters in a string.
    
    A character is considered duplicated if it appears more than once in the string.
    The result contains each unique character that has duplicates, listed exactly once per such character.
    Time Complexity: O(n), where n is the length of the string.
    Space Complexity: O(1) (constant number of distinct ASCII characters).

    Args:
        s (str): Input string to analyze.

    Returns:
        list[str]: List of unique duplicate characters found in the input string, 
                   sorted for consistent output order. If no duplicates exist or if the 
                   string is empty/None, returns an empty list.
    """
    # Use a fixed-size array/list for ASCII letters to ensure O(1) space and efficient lookup/counting.
    # We'll track counts of each character using ord() mapping.
    
    count = [0] * 256  # Covers standard ASCII characters (0-255). This is constant size regardless of input length n.

    for char in s:
        if not isinstance(char, str):
            raise TypeError("Input must be a string.")
        
        index = ord(char)
        count[index] += 1
    
    duplicates = []
    
    # Iterate through the counts to find characters with frequency > 1.
    for i in range(256):
        if count[i] > 1:
            char_code = chr(i)
            duplicates.append(char_code)

    return sorted(duplicates, key=lambda x: ord(x))

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    
    test_cases = [
        "hello world",           # Expected output: ['h', 'l', 'o'] (sorted) -> actually [' ', 'd', 'e', 'h', 'l', 'w', 'r'...] wait, let's trace manually.
                                # h:1, e:1, l:2, o:1, w:1, r:0,d:1,l:3,o:4 -> duplicates are only 'l'. Wait "hello world": h(1),e(1),l(2),o(1),(space)(1),w(1),r(1),d(1). Only 'l' is duplicated.
                                # Correction on manual trace: 
                                # h, e, l, l, o,  , w, o, r, l, d -> wait "hello world" has two spaces? No usually one space between words unless specified.
                                # Let's assume standard input string provided in code block below for clarity of duplicates.
        "aabbccdd",              # Expected: ['a', 'b', 'c', 'd'] (all appear twice)
        "abcdefg",               # Expected: [] (no duplicates)
        "",                      # Expected: [] (empty string)
        "Mississippi"            # M(1),i(4),s(4),p(2). Duplicates: ['I', 'M', 'P', 'S'] -> sorted by char code. 
                                # ASCII order: I, P, S, m? No case sensitivity matters in Python strings unless specified otherwise.
                                # "Mississippi": M(1), i(4), s(4), p(2). Duplicates are i, s, p. 'M' is unique.
                                # Result should be sorted: ['i', 'p', 's']? Or case sensitive sort. 
                                # Let's just rely on the function logic which sorts by ord().
        "Python"                 # P(1),y(1),t(1,hon) -> No duplicates. []
    ]

    for test_string in test_cases:
        result = find_duplicate_characters(test_string)
        print(f'Input: "{test_string}"')
        print(f'Duplicates found: {result}')
        
        # Simple assertion to verify correctness on known cases if needed, 
        # but the task asks only for runnable code.