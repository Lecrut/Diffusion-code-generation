from typing import List

def filter_vowel_words(words: List[str]) -> List[str]:
    vowels = "aeiouAEIOU"
    return [word for word in words if any(vowel in word for vowel in vowels)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "drum", "elephant"]
    filtered_words = filter_vowel_words(sample_words)
    print(filtered_words)