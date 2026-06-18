import argparse

def count_vowels(text: str) -> int:
    """Count vowels in a given string (case-insensitive)."""
    text = text.lower()
    return sum(1 for char in text if char in "aeiou")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Count the total number of vowels in an input.")

    # Create a non-required argument to avoid interactive prompts while allowing usage.
    sample_input_arg = parser.add_argument(
        "--input", "-i", 
        type=str, 
        default=None, 
        help="The word or sentence to analyze (default: uses hardcoded samples)."
    )

    args = parser.parse_args()

    # Hard-coded sample values as per requirement.
    if args.input is None:
        test_cases = [
            "Hello World",
            "Python Programming",
            "aeiouAEIOU"
        ]
        
        for i, word in enumerate(test_cases):
            count = count_vowels(word)
            print(f"Input: '{word}'")
            print(f"Total vowel count: {count}")
    else:
        text_to_analyze = args.input
        
        if not text_to_analyze.strip():
            print("Error: Input cannot be empty.")
        else:
            count = count_vowels(text_to_analyze)
            print(f"Input: '{text_to_analyze}'")
            print(f"Total vowel count: {count}")