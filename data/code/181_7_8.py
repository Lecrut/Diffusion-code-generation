def find_words_with_vowels(words):
    vowels = "aeiouAEIOU"
    return sorted({word for word in words if any(vowel in word for vowel in vowels)})

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    print(find_words_with_vowels(sample_words))