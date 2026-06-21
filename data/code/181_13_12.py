def find_vowel_words(words):
    vowels = 'aeiou'
    vowel_words = [word for word in words if any(char.lower() in vowels for char in word)]
    return vowel_words

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    result = find_vowel_words(sample_words)
    print(result)