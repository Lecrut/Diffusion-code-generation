import sys

def calculate_phrase_length(phrase):
    """Calculate the length of a given phrase."""
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, 
    # network access, or pre-existing files are required.
    
    test_phrases = [
        "Hello World",
        "",
        "Python is awesome!",
        "12345"
    ]

    for phrase in test_phrases:
        try:
            length = calculate_phrase_length(phrase)
            print(f'Phrase: "{phrase}"')
            print(f'Length: {length}')
            print()  # Empty line between outputs
            
        except Exception as e:
            # Graceful handling of any unexpected errors during calculation
            print(f"Error calculating length for phrase '{phrase}': {e}")