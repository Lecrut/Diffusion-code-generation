import argparse
from collections import Counter

def count_vowels(text: str) -> int:
    """Count total vowels in the given text (case-insensitive)."""
    # Define lowercase vowels for comparison
    vowel_set = set("aeiou")
    
    # Convert to lower case and filter characters present in vowel_set
    return sum(1 for char in text.lower() if char in vowel_set)

def main():
    parser = argparse.ArgumentParser(description="Count total vowels in a string.")
    args, _ = parser.parse_known_args()  # Parse knowns but ignore unknown to allow sample input later
    
    # Since the task forbids interactive prompts and requires no user input for the sample block,
    # we will simulate the argument parsing by providing default values directly if none are found.
    
    raw_input_str = ""
    if args:
        # If arguments were passed (e.g., from command line), take the first one as the string
        raw_input_str = " ".join(args)
    else:
        # Default sample value for execution without user input
        raw_input_str = "Hello, World! This is a test sentence."

    vowel_count = count_vowels(raw_input_str)
    
    print(f"Total vowels found in '{raw_input_str}': {vowel_count}")

if __name__ == '__main__':
    main()