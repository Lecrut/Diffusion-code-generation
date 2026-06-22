import re

VOWELS = 'aeiouAEIOU'

def remove_vowels(text):
    pattern = f"[{re.escape(VOWELS)}]"
    return re.sub(pattern, '', text)

if __name__ == '__main__':
    sample_text = "Hello, World!"
    print(remove_vowels(sample_text))