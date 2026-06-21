def extract_vowel_words(words):
    vowels = "aeiouAEIOU"
    return [word for word in words if any(vowel in word for vowel in vowels)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "drum", "echo"]
    print(extract_vowel_words(sample_words))