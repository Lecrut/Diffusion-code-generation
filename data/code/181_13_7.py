import re

def check_vowel_presence(words):
    vowels = 'aeiouAEIOU'
    return [any(char in vowels for char in word) for word in words]

if __name__ == '__main__':
    sample_words = ['hello', 'world', 'Python', 'programming']
    print(check_vowel_presence(sample_words))