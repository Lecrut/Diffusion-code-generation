# Command-line script to calculate phrase length
# This module demonstrates calculating string length without interactive prompts in the main execution block.

def get_phrase_length(phrase: str) -> int:
    """Returns the exact length of the provided phrase."""
    return len(phrase)

if __name__ == '__main__':
    # Sample values to run without user input, network access, or pre-existing files
    sample_phrases = ["Hello", "Python Programming"]

    for phrase in sample_phrases:
        length = get_phrase_length(phrase)
        print(length)