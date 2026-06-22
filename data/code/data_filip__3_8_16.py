import re

def strip_vowels(text: str) -> str:
    return re.sub(r'[aeiouAEIOU]', '', text)

if __name__ == '__main__':
    result = strip_vowels('Hello World')
    print(result)