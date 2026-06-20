import re

def remove_vowels(s):
    return re.sub(r'[aeiouAEIOU]', '', s)

if __name__ == '__main__':
    print(remove_vowels("Hello World"))
    print(remove_vowels("Python Programming"))
    print(remove_vowels("AEIOU aeiou"))