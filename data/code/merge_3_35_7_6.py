def count_vowels(word: str) -> int:
    """Returns the total number of vowels in the given word."""
    return sum(1 for char in word if char.lower() in 'aeiou')

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or network access.
    test_words = [
        "hello", 
        "skydiver", 
        "rhythm"
    ]

    for word in test_words:
        vowel_count = count_vowels(word)
        print(f"The total vowel count in '{word}' is {vowel_count}.")