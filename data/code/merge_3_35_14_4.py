import argparse

def count_vowels(text: str) -> int:
    """Counts the total number of vowels in a given string."""
    text = text.lower()
    return sum(1 for char in text if char in "aeiou")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Count vowels in a sentence.")
    # Using an optional argument to avoid requiring user input via stdin
    args = parser.parse_args(["--sample", "Hello, world!"])

    sample_word_or_sentence: str = args.sample if hasattr(args, 'sample') else ""
    
    result_count = count_vowels(sample_word_or_sentence)
    print(f"Total vowel count for '{sample_word_or_sentence}': {result_count}")