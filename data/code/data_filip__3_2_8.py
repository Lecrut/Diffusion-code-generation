import re

def remove_vowels(text: str) -> str:
    return re.sub(r'[aeiouAEIOU]', '', text)

if __name__ == '__main__':
    text = "Hello World"
    result = remove_vowels(text)
    print(result)