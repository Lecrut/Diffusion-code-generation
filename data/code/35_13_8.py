def count_vowels(text: str) -> int:
    """Returns the total number of vowel characters in the given string."""
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    test_strings = ["Hello, World!", "Python Programming", "æöüÅÄÖ"]
    for s in test_strings:
        print(f"'{s}' has {count_vowels(s)} vowel(s)")