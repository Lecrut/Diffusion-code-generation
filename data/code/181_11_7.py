def has_vowel(word: str) -> bool:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return any(char in vowels for char in word.lower())

def find_vowel_words(words: list[str]) -> list[str]:
    return [word for word in words if has_vowel(word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "drum", "elephant"]
    result = find_vowel_words(sample_words)
    print(result)