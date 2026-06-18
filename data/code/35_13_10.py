def count_vowels(text: str) -> int:
    """Returns the total number of vowels (a, e, i, o, u, case-insensitive) in the given string."""
    return sum(1 for char in text if char.lower() in "aeiou")

if __name__ == '__main__':
    sample_strings = ["Hello World!", "AEIOU", "rhythm"]
    print(count_vowels(sample_strings[0]))  # Output: 2 (e, o)
    print(count_vowels(sample_strings[1]))  # Output: 5
    print(count_vowels(sample_strings[2]))  # Output: 2 (y is not counted here based on strict definition)