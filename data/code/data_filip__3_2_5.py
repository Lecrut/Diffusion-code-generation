import re

def remove_vowels(text):
    return re.sub(r'[aeiouAEIOU]', '', text)

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "Python Programming"
    sample3 = "AEIOU aeiou 123"
    print(remove_vowels(sample1))
    print(remove_vowels(sample2))
    print(remove_vowels(sample3))