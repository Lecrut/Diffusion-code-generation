def find_repeated_letters(text: str) -> list[str]:
    """
    Identifies all letters that appear more than once in the input string.
    
    The function is case-insensitive, treating 'A' and 'a' as the same letter.
    It ignores non-alphabetic characters (digits, spaces, punctuation).
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of unique repeated letters found in lowercase.
                   If no repetitions are found, returns an empty list.
    """
    # Dictionary to count occurrences of each letter
    char_count = {}
    
    # Iterate through the text and convert characters to lowercase for case-insensitivity
    for char in text.lower():
        if 'a' <= char <= 'z':  # Check if character is an alphabetic letter
            char_count[char] = char_count.get(char, 0) + 1
            
    # Collect letters that have a count greater than 1 and sort them alphabetically
    repeated_letters = sorted([letter for letter, count in char_count.items() if count > 1])
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    test_cases = [
        "Hello World!",           # Expected: ['e', 'l'] (case-insensitive)
        "Python Programming",     # Expected: ['n', 'r']
        "The Quick Brown Fox Jumps Over The Lazy Dog.",  # Expected: ['t', 'h', 'e']
        "No Repetitions Here!",   # Expected: []
        "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz",  # All letters repeated
    ]

    for test_string in test_cases:
        result = find_repeated_letters(test_string)
        print(f"Input: '{test_string}'")
        if not result:
            print("Repeated letters found: None")
        else:
            print(f"Repeated letters found: {', '.join(result)}")
        print("-" * 40)