def find_repeated_letters(sentence: str) -> set:
    """
    Identifies all letters that appear more than once in a given sentence.
    
    Uses a dictionary to count occurrences of each character, then filters 
    those with a count greater than 1. Only alphabetic characters are considered.
    
    Args:
        sentence (str): The input string to analyze.
        
    Returns:
        set: A set containing the repeated letters in lowercase.
    """
    char_count = {}
    
    # Iterate through each character in the sentence
    for char in sentence.lower():  # Convert to lowercase for case-insensitive comparison
        if 'a' <= char <= 'z':  # Ensure only alphabetic characters are counted
            count = char_count.get(char, 0) + 1
            char_count[char] = count
            
    # Extract letters that have been seen more than once
    repeated_letters = {letter for letter, count in char_count.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies
    test_sentences = [
        "Hello World",
        "Python Programming is Fun!",
        "The quick brown fox jumps over the lazy dog"
    ]
    
    for sentence in test_sentences:
        result = find_repeated_letters(sentence)
        if result:
            print(f"'{sentence}' -> Repeated letters: {sorted(result)}")
        else:
            print(f"'{sentence}' -> No repeated letters found.")