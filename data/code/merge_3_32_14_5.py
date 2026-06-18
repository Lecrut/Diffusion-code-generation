def get_phrase_length(phrase):
    """Calculate the length of a phrase string."""
    return len(phrase)

if __name__ == '__main__':
    # Sample values to ensure execution without user input or errors
    sample_values = [
        "Hello, World!",
        "",
        "A" * 100,
        None,   # Simulating a potential error case if handled later
        ""      # Edge case: empty string
    ]

    for phrase in sample_values:
        try:
            if phrase is None or not isinstance(phrase, str):
                print(f"Input validation failed for '{phrase}'. Expected a string.")
            else:
                length = get_phrase_length(phrase)
                print(f"The length of the provided phrase ('{phrase}') is {length}.")
        except Exception as e:
            # Graceful error handling for any unexpected issues
            print(f"An error occurred while processing '{phase}': {e}")

    # Additional hardcoded direct test to demonstrate functionality without input prompt
    final_phrase = "Python Programming Challenges!"
    calculated_length = get_phrase_length(final_phrase)
    assert calculated_length == len(final_phrase), "Calculation mismatch detected."
    
    print(f"Final verification: Length of '{final_phrase}' is {calculated_length}.")