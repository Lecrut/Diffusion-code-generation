def contains_vowel(word):
    vowels = set('aeiouAEIOU')
    return any(char in vowels for char in word)

def extract_vowel_words(strings):
    result = []
    for string in strings:
        words_with_vowels = [word for word in string.split() if contains_vowel(word)]
        result.append(words_with_vowels)
    return result

if __name__ == '__main__':
    sample_strings = ["Hello world", "Python programming", "Data science"]
    print(extract_vowel_words(sample_strings))