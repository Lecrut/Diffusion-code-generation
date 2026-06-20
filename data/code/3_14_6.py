import re

def remove_vowels(text: str) -> str:
    pattern = re.compile(r'[aeiouAEIOU]')
    return pattern.sub('', text)

if __name__ == '__main__':
    input_text = "Hello World"
    result = remove_vowels(input_text)
    print(result)