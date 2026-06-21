import re

def check_vowel_presence(words):
    vowels = 'aeiouAEIOU'
    return [any(v in word for v in vowels) for word in words]

if __name__ == '__main__':
    sample_words = ['hello', 'world', 'Python', 'regex']
    print(check_vowel_presence(sample_words))