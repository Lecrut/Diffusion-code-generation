def calculate_phrase_length(phrase):
    """Calculate the length of a given phrase."""
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or arguments
    test_phrases = [
        "Hello, World!",
        "",
        "Python scripting is fun.",
        "!@#$%^&*()",
    ]

    for phrase in test_phrases:
        try:
            length = calculate_phrase_length(phrase)
            print(f"Phrase: '{phrase}'")
            print(f"Length: {length}")
        except Exception as e:
            # Graceful handling of any unexpected errors during calculation
            print(f"Error processing phrase: {e}")