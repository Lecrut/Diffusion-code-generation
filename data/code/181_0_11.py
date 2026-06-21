def extract_vowel_words(strings):
    vowels = set('aeiouAEIOU')
    
    def contains_vowel(word):
        return any(char in vowels for char in word)
    
    return [word for string in strings for word in string.split() if contains_vowel(word)]

if __name__ == '__main__':
    sample_strings = ["Hello world", "Python programming", "Data science"]
    print(extract_vowel_words(sample_strings))