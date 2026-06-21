def has_vowels(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return any(char in vowels for char in word.lower())

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "grape"]
    vowel_presence = {word: has_vowels(word) for word in sample_words}
    print(vowel_presence)