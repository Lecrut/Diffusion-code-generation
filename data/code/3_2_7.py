import re

def remove_vowels(text: str) -> str:
    return re.sub(r'[aeiouAEIOU]', '', text)

if __name__ == '__main__':
    sample_text = "Hello World"
    result = remove_vowels(sample_text)
    print(result)