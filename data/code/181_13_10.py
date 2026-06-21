import re

def check_vowels(words):
    vowels = 'aeiouAEIOU'
    result = []
    for word in words:
        has_vowel = any(char in vowels for char in word)
        result.append((word, has_vowel))
    return result

if __name__ == '__main__':
    sample_words = ['apple', 'sky', 'banana', 'cherry']
    print(check_vowels(sample_words))