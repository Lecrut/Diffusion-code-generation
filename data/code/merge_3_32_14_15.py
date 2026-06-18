def calculate_phrase_length(phrase):
    """Calculate the length of a given phrase."""
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or network access
    samples = ["Hello, World!", "Python scripting is fun.", "", "12345"]

    for test_phrase in samples:
        try:
            length = calculate_phrase_length(test_phrase)
            print(f"Phrase: '{test_phrase}'")
            print(f"Length: {length}")
        except Exception as e:
            # Graceful error handling, though unlikely with len() on strings
            print(f"Error processing phrase: {e}")

    # Simulating a potential input error scenario (empty string or non-string)
    try:
        invalid_input = 12345  # Not a string
        length_invalid = calculate_phrase_length(invalid_input)
        print(f"Length of '{invalid_input}': {length_invalid}")
    except TypeError as e:
        print("Handled input error gracefully:", str(e))

    # Final confirmation run with a valid sample
    final_sample = "Command-line utility test."
    final_len = calculate_phrase_length(final_sample)
    print(f"Final Test - Phrase length of '{final_sample}': {final_len}")