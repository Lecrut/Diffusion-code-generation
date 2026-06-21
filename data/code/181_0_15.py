def extract_vowel_words(strings):
    vowels = "aeiouAEIOU"
    words_with_vowels = []
    for string in strings:
        words = string.split()
        vowel_words = [word for word in words if any(char in vowels for char in word)]
        words_with_vowels.extend(vowel_words)
    return words_with_vowels

if __name__ == '__main__':
    sample_strings = ["Hello world", "Python programming", "Data science"]
    result = extract_vowel_words(sample_strings)
    print(result)