import re

def remove_vowels(text: str) -> str:
    pattern = re.compile(r'[aeiouAEIOU]')
    return pattern.sub('', text)

if __name__ == '__main__':
    result = remove_vowels("Hello World")
    print(result)