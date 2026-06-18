def find_repeated_letters(text: str) -> list[str]:
    """
    Identifies all letters that appear more than once in the input string, 
    regardless of case (e.g., 'A' and 'a' are considered the same letter).
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of unique repeated letters found.
                   If no repeats exist, returns an empty list.
    """
    # Convert to lowercase for case-insensitive comparison and filter out non-letter characters
    cleaned_text = [char.lower() for char in text if char.isalpha()]
    
    letter_counts = {}
    
    # Count occurrences of each letter
    for letter in cleaned_text:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    
    # Extract letters with a count greater than 1 and sort them alphabetically
    repeated_letters = sorted([letter for letter, count in letter_counts.items() if count > 1])
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    test_cases = [
        "Hello World",          # Expected: ['e', 'l'] (case-insensitive)
        "A man, a plan, a canal: Panama!",  # Expected: ['a', 'n', 'p']
        "abcdef",               # Expected: []
        "The quick brown fox jumps over the lazy dog.", 
    ]

    for test_string in test_cases:
        result = find_repeated_letters(test_string)
        print(f"Input: \"{test_string}\"")
        if result:
            repeated_chars_str = ", ".join(result)
            print(f"Repeated letters found: {repeated_chars_str}")
        else:
            print("No repeated letters found.")
        print("-" * 30)