def find_vowel_words(words):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return [word for word in words if any(char.lower() in vowels for char in word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "drum"]
    result = find_vowel_words(sample_words)
    print(result)