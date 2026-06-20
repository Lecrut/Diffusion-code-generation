import re

def strip_vowels(s):
    return re.sub(r'[aeiouAEIOU]', '', s)

if __name__ == '__main__':
    print(strip_vowels("Hello World"))
    print(strip_vowels("Python Programming"))
    print(strip_vowels("AEIOU aeiou"))