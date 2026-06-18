import sys

def calculate_phrase_length(phrase: str) -> int:
    """Calculate the length of a given phrase."""
    return len(phrase)

def main():
    # Simulate user input with hard-coded sample values as per requirements.
    # This ensures no actual input(), sys.stdin, or network access is used.
    test_phrases = ["Hello World", "Python scripting", "", "   ", "!@#"]

    for phrase in test_phrases:
        try:
            length = calculate_phrase_length(phrase)
            print(f"Phrase: '{phrase}'")
            print(f"Length: {length}")
        except Exception as e:
            # Graceful handling of any unexpected errors during calculation.
            print(f"Error processing phrase: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()