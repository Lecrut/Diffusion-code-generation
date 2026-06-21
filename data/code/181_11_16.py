from typing import List

def filter_vowel_words(words: List[str]) -> List[str]:
    vowels = "aeiouAEIOU"
    return [word for word in words if any(char in vowels for char in word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "drum", "elephant"]
    print(filter_vowel_words(sample_words))