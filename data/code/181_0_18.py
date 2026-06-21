VOWELS = set('aeiouAEIOU')

def extract_vowel_words(strings):
    return [''.join(word) for string in strings for word in string.split() if any(char in VOWELS for char in word)]

if __name__ == '__main__':
    sample_strings = ["Hello world", "Python programming", "Data science"]
    print(extract_vowel_words(sample_strings))