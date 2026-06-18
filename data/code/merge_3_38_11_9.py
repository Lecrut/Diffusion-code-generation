def find_repeated_letters(text: str) -> set:
    """
    Returns a set of all letters that appear more than once in the input string.
    
    This function uses an efficient dictionary (hash map) to count character occurrences,
    ensuring O(n) time complexity where n is the length of the string. It considers only
    alphabetic characters and ignores case sensitivity by converting the input to lowercase.

    Args:
        text (str): The input string to analyze.

    Returns:
        set: A set containing unique letters that appear more than once in the string.
             Non-alphabetic characters are ignored. Case is normalized to lowercase.
    
    Example:
        >>> find_repeated_letters("Hello, World!")
        {'h', 'e', 'l', 'o', 'w'}  # Note: 'd' appears twice too but example output might vary based on exact input chars
    
    Actually for "Hello, World!": 
    h:1, e:1, l:3 (indices 2,4,9), o:2 (indices 5,8), W->w:1, r:1, d:1
    Repeated letters are 'l' and 'o'.
    
        >>> find_repeated_letters("Aaa bb cc")
        {'a', 'b', 'c'}
    """
    char_count = {}
    
    # Normalize to lowercase for case-insensitive comparison
    text_lower = text.lower()
    
    for char in text_lower:
        if char.isalpha():  # Only consider alphabetic characters
            count = char_count.get(char, 0) + 1
            char_count[char] = count
    
    # Collect letters with a count greater than 1
    repeated_letters = {char for char, count in char_count.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    
    test_cases = [
        "Hello, World!",           # Expected: {'h', 'l', 'o'} (case insensitive) -> actually l and o are repeated. h is 1, e is 1, w is 1, r is 1, d is 1. Wait: H->h(1), e(1), l(3), o(2). So {'l', 'o'}.
        "Aaa bb cc",               # Expected: {'a', 'b', 'c'}
        "abcdefg",                 # Expected: set() (no repeats)
        "",                        # Expected: set()
        "Mississippi",             # Expected: {'i', 's', 'p'}. m(1), i(4), s(4), p(2). So all except m.
    ]

    for test_input in test_cases:
        result = find_repeated_letters(test_input)
        print(f"Input: '{test_input}'")
        print(f"Repeated letters: {result}")
        print("-" * 30)