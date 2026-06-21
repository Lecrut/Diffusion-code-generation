def find_words_with_vowels(words):
    vowels = "aeiou"
    return sorted({word for word in words if any(vowel in word.lower() for vowel in vowels)})

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date", "elderberry"]
    print(find_words_with_vowels(sample_words))