def count_vowels(text: str) -> int:
    """Count vowels (both uppercase and lowercase) in a string."""
    return sum(1 for char in text.lower() if char in "aeiou")

if __name__ == '__main__':
    samples = ["Hello, World!", "AEIOU", "Python3.9", "", "aEiOu"]
    print("Vowel counts:")
    for word in samples:
        print(f"'{word}' -> {count_vowels(word)}")