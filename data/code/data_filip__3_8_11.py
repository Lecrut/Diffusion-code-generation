import re

def strip_vowels(text):
    if not text:
        return text
    pattern = re.compile(r'[aeiouAEIOU]')
    return pattern.sub('', text)

if __name__ == '__main__':
    sample_text = "Hello World"
    result = strip_vowels(sample_text)
    print(result)