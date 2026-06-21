def extract_vowel_words(strings):
    vowels = set('aeiouAEIOU')
    result = []
    for string in strings:
        words = string.split()
        vowel_words = [''.join(filter(lambda char: char in vowels, word)) for word in words]
        if vowel_words:
            result.append(' '.join(vowel_words))
    return result

if __name__ == '__main__':
    sample_strings = ["Hello world", "Python programming", "Data science"]
    print(extract_vowel_words(sample_strings))