import re

def check_vowel_presence(words):
    vowels = 'aeiouAEIOU'
    return [any(vow in word for vow in vowels) for word in words]

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry', 'drum']
    print(check_vowel_presence(sample_words))