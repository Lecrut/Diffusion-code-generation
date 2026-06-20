import re

_vowel_re = re.compile(r'[aeiouAEIOU]')

def remove_vowels(s):
    return _vowel_re.sub('', s)

if __name__ == '__main__':
    print(remove_vowels('hello world'))
    print(remove_vowels('Python Programming'))
    print(remove_vowels('AEIOU'))
    print(remove_vowels('xyz'))