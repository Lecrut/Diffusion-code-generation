def extract_words_with_vowels(strings):
    vowels = "aeiouAEIOU"
    return [word for word in strings if any(vowel in word for vowel in vowels)]

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "drum", "elephant"]
    print(extract_words_with_vowels(sample_strings))