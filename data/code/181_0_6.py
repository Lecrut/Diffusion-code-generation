def extract_vowel_words(strings):
    vowels = "aeiouAEIOU"
    return [''.join(filter(lambda char: char in vowels, word)) for string in strings for word in string.split()]

if __name__ == '__main__':
    sample_strings = ["Hello world", "Python programming", "Data Science"]
    print(extract_vowel_words(sample_strings))