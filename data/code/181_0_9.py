def has_vowel(word):
    vowels = set('aeiouAEIOU')
    return any(char in vowels for char in word)

def extract_vowel_words(strings):
    return [word for string in strings for word in string.split() if has_vowel(word)]

if __name__ == '__main__':
    sample_strings = ["Hello world", "Python programming", "Data science"]
    print(extract_vowel_words(sample_strings))