import re

VOWELS = 'aeiouAEIOU'
REMOVE_VOWEL_PATTERN = f"[{re.escape(VOWELS)}]"

def remove_vowels(text):
    return re.sub(REMOVE_VOWEL_PATTERN, '', text)

if __name__ == '__main__':
    sample_text = "Hello, World!"
    print(remove_vowels(sample_text))