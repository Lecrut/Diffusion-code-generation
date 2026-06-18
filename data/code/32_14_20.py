def calculate_phrase_length(phrase):
    """Calculate the length of a given phrase."""
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values to avoid interactive input requirements
    test_phrases = [
        "Hello, World!",
        "",
        "Python scripting is fun",
        "!@#$%^&*()",
    ]

    for phrase in test_phrases:
        try:
            length = calculate_phrase_length(phrase)
            print(f"Phrase: '{phrase}'")
            print(f"Length: {length}")
            print("---")  # Separator between samples
        except Exception as e:
            print(f"Error processing phrase: {e}")