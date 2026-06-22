import re

_vowel_re = re.compile(r'[aeiouAEIOU]')

def remove_vowels(text):
    return _vowel_re.sub('', text)

if __name__ == '__main__':
    print(remove_vowels("Hello World"))
    print(remove_vowels("Python Programming"))
    print(remove_vowels("AEIOU aeiou"))
    print(remove_vowels("No Vowels Here"))