import sys

def calculate_phrase_length(phrase):
    """Calculates the length of a given phrase."""
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or files
    test_phrases = [
        "Hello, World!",
        "",
        "Python is awesome.",
        "!@#$%^&*()"
    ]

    for phrase in test_phrases:
        try:
            length = calculate_phrase_length(phrase)
            print(f"Phrase: '{phrase}'")
            print(f"Length: {length}")
        except Exception as e:
            # Graceful handling of any unexpected errors during calculation
            print(f"Error processing phrase: {e}", file=sys.stderr)