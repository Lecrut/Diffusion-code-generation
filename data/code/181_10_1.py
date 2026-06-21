def extract_words_with_vowels(words):
    vowels = "aeiouAEIOU"
    return [word for word in words if any(vowel in word for vowel in vowels)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "grape", "kiwi"]
    print(extract_words_with_vowels(sample_words))