def count_vowels(text):
    """Counts the total number of vowels in a given string."""
    text = text.lower()
    return sum(1 for char in text if char in 'aeiou')

if __name__ == '__main__':
    sample_words = ["hello", "programming", "rhythm"]
    results = []

    for word in sample_words:
        count = count_vowels(word)
        print(f"Word: {word}, Vowel Count: {count}")