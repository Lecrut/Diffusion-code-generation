import re

_remove_vowels_re = re.compile(r'[aeiouAEIOU]')

def remove_vowels(s):
    return _remove_vowels_re.sub('', s)

if __name__ == '__main__':
    print(remove_vowels('Hello World'))
    print(remove_vowels('Python Programming'))
    print(remove_vowels(''))
    print(remove_vowels('bcdfg'))
    print(remove_vowels('AEIOU aeiou'))