from typing import List

def filter_vowel_words(words: List[str]) -> List[str]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return [word for word in words if any(char.lower() in vowels for char in word)]

if __name__ == '__main__':
    sample_words = ["This", "is", "a", "test", "sentence", "with", "some", "words", "like", "programming", "and", "education"]
    result = filter_vowel_words(sample_words)
    print(result)