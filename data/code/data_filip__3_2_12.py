import re

def remove_vowels(text: str) -> str:
    return re.sub(r'[aeiouAEIOU]', '', text)

if __name__ == '__main__':
    sample = "Hello World"
    print(remove_vowels(sample))