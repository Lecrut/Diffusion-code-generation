def find_repeated_letters(text: str) -> set:
    """
    Returns a set of all letters that appear more than once in the input string.
    
    This function uses an efficient dictionary (hash map) to count character occurrences,
    ensuring O(n) time complexity where n is the length of the string. It considers only
    alphabetic characters and ignores case sensitivity by converting to lowercase.

    Args:
        text (str): The input string to analyze.

    Returns:
        set: A set containing unique letters that appear more than once in the string.
             Non-alphabetic characters are ignored, and duplicates within a letter type 
             do not affect its inclusion or exclusion from the result.
    
    Example:
        >>> find_repeated_letters("Hello World")
        {'h', 'e', 'l', 'o', 'w'}  # Note: case-insensitive comparison used
    
    """
    char_count = {}

    for char in text.lower():
        if char.isalpha():
            count = char_count.get(char, 0) + 1
            char_count[char] = count

    repeated_letters = {char for char, count in char_count.items() if count > 1}

    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_cases = [
        "Hello World",           # Expected: {'h', 'e', 'l', 'o', 'w'} (case-insensitive)
        "A man, a plan, a canal: Panama!",  # Expected: {'a', 'n', 'p'}. Note: case insensitive.
        "abcdefg",               # Expected: set() - no repeated letters
        "aaaaabbbbccccddddeeee",# Expected: {'a', 'b', 'c', 'd', 'e'}
    ]

    for test_input in test_cases:
        result = find_repeated_letters(test_input)
        print(f"Input: '{test_input}'")
        print(f"Repeated letters: {sorted(result)}\n")  # Sorted for consistent output display.