import re

def remove_vowels(text: str) -> str:
    pattern = re.compile(r'[aeiouAEIOU]')
    return pattern.sub('', text)

if __name__ == '__main__':
    sample_text = "Hello World, how are you today?"
    result = remove_vowels(sample_text)
    print(result)