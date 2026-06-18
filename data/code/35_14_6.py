import argparse

def count_vowels(text: str) -> int:
    """Counts the total number of vowels (a, e, i, o, u) in a string."""
    vowel_set = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowel_set)

def main():
    parser = argparse.ArgumentParser(description="Count the total number of vowels in an input sentence.")
    
    # Since we cannot use interactive prompts or required arguments as per constraints, 
    # we define a non-optional argument that will be populated by sample values.
    text_input = parser.add_argument('text', help='The word or sentence to analyze.')

    args = parser.parse_args()
    input_word = args.text

# The following block provides the required hard-coded sample value and runs without user interaction.
if __name__ == '__main__':
    # Hard-coded sample values as requested; no network access, files, or stdin used here.
    sample_words = [
        "Hello World",
        "aeiouAEIOU",
        "rhythm"
    ]

    for word in sample_words:
        count = count_vowels(word)
        print(f"'{word}' has {count} vowel(s).")