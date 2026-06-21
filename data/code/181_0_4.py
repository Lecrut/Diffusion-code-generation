def extract_vowel_words(strings):
    vowels = "aeiouAEIOU"
    return [word for s in strings for word in s.split() if any(v in word for v in vowels)]

if __name__ == '__main__':
    sample_strings = ["Hello world", "Python programming", "Is this a test"]
    print(extract_vowel_words(sample_strings))