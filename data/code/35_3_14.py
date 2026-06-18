from string import ascii_lowercase as vowels_lower

def count_vowels(s: str) -> int:
    return sum(1 for char in s.lower() if char in set(vowels_lower))

if __name__ == '__main__':
    test_strings = ["Hello, World!", "AEIOU", "aeiou"]
    for text in test_strings:
        print(f"Vowel count in '{text}': {count_vowels(text)}")