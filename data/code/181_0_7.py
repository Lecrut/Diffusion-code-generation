def extract_vowel_words(strings):
    vowels = set('aeiouAEIOU')
    return [''.join(word for word in string.split() if any(char in vowels for char in word)) for string in strings]

if __name__ == '__main__':
    sample_strings = ["Hello world", "Python programming", "Data science"]
    print(extract_vowel_words(sample_strings))