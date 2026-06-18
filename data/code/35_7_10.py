import string

def count_vowels(word: str) -> int:
    """Counts the total number of vowels in a given word (case-insensitive)."""
    return sum(1 for char in word.lower() if char in 'aeiou')

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, stdin usage, or network access is required.
    test_cases = ["hello", "beautiful day", "rhythm"]

    for test_word in test_cases:
        vowel_count = count_vowels(test_word)
        print(f"Word: '{test_word}'")
        print(f"Total vowels: {vowel_count}")