def filter_vowel_words(words):
    vowels = "aeiouAEIOU"
    return [word for word in words if any(char in vowels for char in word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    print(filter_vowel_words(sample_words))