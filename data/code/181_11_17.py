def filter_vowel_words(words):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return [word for word in words if any(char in vowels for char in word.lower())]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "dog", "elephant"]
    result = filter_vowel_words(sample_words)
    print(result)