import re

_remove_vowels_re = re.compile(r'[aeiouAEIOU]')

def remove_vowels(s):
    return _remove_vowels_re.sub('', s)

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "AEIOUaeiou"
    sample3 = "Python Programming"
    print(remove_vowels(sample1))
    print(remove_vowels(sample2))
    print(remove_vowels(sample3))