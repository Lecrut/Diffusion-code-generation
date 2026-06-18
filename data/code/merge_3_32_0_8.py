def calculate_string_length(s):
    """
    Calculate the length of a given string efficiently handling both ASCII 
    and Unicode characters (including emojis, accented letters, etc.).
    
    In Python 3, strings are unicode by default, so len() handles all cases correctly.
    This function simply returns the standard length to ensure efficiency without
    unnecessary overhead or external dependencies.

    Args:
        s (str): The input string whose length is to be calculated.

    Returns:
        int: The number of characters in the string, including multi-byte Unicode 
             sequences like emojis and accented letters.
    
    Example:
        >>> calculate_string_length("Hello 世界 🌍")
        12
    """
    return len(s)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        "Simple ASCII",           # Expected: 13 (spaces included)
        "Unicode chars éàüñ",     # Expected: 9 (accented letters count as 1 char each in Python strings)
        "Emoji example 🎉🚀💡",    # Expected: 14 (emojis are single characters/strings in Py3)
        "",                       # Edge case: Empty string, Expected: 0
        "Special chars <>&\"'",   # Expected: 9
    ]

    for i, test_input in enumerate(test_cases):
        result = calculate_string_length(test_input)
        print(f"Test {i + 1}: Input='{test_input}' -> Length={result}")