import sys

def reverse_word(word: str) -> str:
    """Returns the reversed version of the input word."""
    return word[::-1]

if __name__ == '__main__':
    # Sample values to run without user interaction
    sample_words = ["hello", "world", "!"]

    for test_input in sample_words:
        print(f"Original: {test_input}")
        reversed_word = reverse_word(test_input)
        print(f"Reversed: {reversed_word}")
        
        # Simulate a friendly output summary if multiple samples are processed
        if len(sample_words) > 1 and test_input == sample_words[-1]:
            print("\nSample execution completed successfully.")

    # Prevent any accidental prompts by redirecting stdin to empty string in this specific context,
    # though the logic above ensures no input() calls occur. 
    sys.stdout.flush()