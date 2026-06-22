import re

def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

def remove_vowels(text):
    pattern = r'[aeiouAEIOU]'
    return re.sub(pattern, '', text)

if __name__ == '__main__':
    sample_text = "Hello, World!"
    validate_input(sample_text)
    print(remove_vowels(sample_text))