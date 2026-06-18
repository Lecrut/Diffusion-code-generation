def find_repeated_letters(text: str) -> set:
    """
    Returns a set of all letters that appear more than once in the input string.
    
    The function uses a dictionary to count occurrences efficiently (O(n)) and 
    filters out characters with counts greater than 1. Only alphabetic characters 
    are considered, ignoring case sensitivity by converting to lowercase first.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        set: A set of unique letters that appear more than once in the string.
    """
    letter_counts = {}
    
    # Iterate through each character, convert to lowercase for case-insensitivity
    for char in text.lower():
        if 'a' <= char <= 'z':  # Ensure only alphabetic characters are considered
            count = letter_counts.get(char, 0) + 1
            letter_counts[char] = count
            
    # Extract letters with a count greater than 1 into a set for uniqueness and O(1) lookup
    repeated_letters = {char for char, count in letter_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    test_cases = [
        "hello world",      # Expected: {'h', 'l', 'o'} (case-insensitive, spaces ignored)
        "aabbccdd",         # Expected: {'a', 'b', 'c', 'd'}
        "abcdefg",          # Expected: set() - no repeated letters
        "The Quick Brown Fox Jumps Over The Lazy Dog",  # Expected: {'t', 'h', 'e'} (case-insensitive)
    "Mississippi"           # Expected: {'i', 's', 'p'}
    ]

    for test_input in test_cases:
        result = find_repeated_letters(test_input)
        print(f"Input: '{test_input}' -> Output: {result}")