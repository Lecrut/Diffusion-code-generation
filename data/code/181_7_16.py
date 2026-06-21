def find_vowel_words(words):
    vowels = "aeiouAEIOU"
    return sorted({word for word in words if any(vowel in word for vowel in vowels)})

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date", "fig", "grape"]
    print(find_vowel_words(sample_words))