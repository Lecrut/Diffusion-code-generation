import re

_vowel_re = re.compile(r'[aeiouAEIOU]')

def remove_vowels(text: str) -> str:
    return _vowel_re.sub('', text)

if __name__ == '__main__':
    result = remove_vowels("Hello World")
    print(result)