def count_vowels(word: str) -> int:
    """Counts the total number of vowels in a given word."""
    return sum(1 for char in word if char.lower() in 'aeiou')

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    test_cases = [
        "hello",
        "programming",
        "beautiful",
        "",
        "AEIOU"
    ]

    for word in test_cases:
        vowel_count = count_vowels(word)
        print(f"The total vowel count in '{word}' is {vowel_count}.")