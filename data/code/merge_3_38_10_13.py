def find_repeated_letters(text: str) -> list[str]:
    """
    Identifies all letters that appear more than once in the input string, 
    regardless of case (treats 'A' and 'a' as the same letter).
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of unique repeated letters found.
                   If no repetitions are found, returns an empty list.
    """
    # Convert to lowercase for case-insensitive comparison and filter out non-alphabetic characters
    processed_text = [char.lower() for char in text if char.isalpha()]
    
    letter_counts = {}
    repeated_letters = []

    for letter in processed_text:
        if letter in letter_counts:
            # If the count is already > 1, we don't need to add it again 
            # because we only want unique letters. However, checking here ensures accuracy.
            pass
        
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    for letter in processed_text:
        if letter_counts[letter] > 1 and letter not in repeated_letters:
            repeated_letters.append(letter)

    # Sort the list to ensure consistent output order (e.g., alphabetical)
    return sorted(repeated_letters)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, command-line arguments, or network access is used here.
    
    test_cases = [
        "Hello World",           # Expected: ['h', 'l'] (case-insensitive) -> sorted: ['h', 'l']
        "A man a plan a canal Panama!",  # Expected: ['a', 'm', 'n', 'p'] 
        "Python Programming",   # Expected: ['o', 'r', 'p']
        "Unique Letters Here",  # Expected: [] (no repeats)
        "The quick brown fox jumps over the lazy dog"  # Complex sentence test
    ]

    for sample in test_cases:
        result = find_repeated_letters(sample)
        print(f"Input: '{sample}'")
        if not result:
            print("No repeated letters found.")
        else:
            print(f"Repeated letters: {', '.join(result)}")
        
        # Optional separator for clarity in console output
        print("-" * 40)