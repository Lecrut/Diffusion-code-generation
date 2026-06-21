from typing import List

def filter_words_with_vowels(words: List[str]) -> List[str]:
    vowels = "aeiouAEIOU"
    return [word for word in words if any(vowel in word for vowel in vowels)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "drum"]
    filtered_words = filter_words_with_vowels(sample_words)
    print(filtered_words)