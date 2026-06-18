import argparse

def count_vowels(text: str) -> int:
    """Return the total number of vowels (a, e, i, o, u) in a string."""
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count total vowels in the input.")

    # No required arguments, so user provides sample data via CLI flags for demonstration.
    parser.add_argument("word", nargs=3, help="Three words to count vowels separately (for demo).")
    
    args = parser.parse_args()
    
    results = [count_vowels(word) for word in args.word]
    
    # Displaying the total vowel count across all three sample inputs.
    print(f"Total vowel count: {sum(results)}")