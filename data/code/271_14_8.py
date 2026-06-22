import re

def remove_vowels(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    pattern = r'[aeiouAEIOU]'
    return re.sub(pattern, '', text)

if __name__ == '__main__':
    sample_text = "Hello, World!"
    print(remove_vowels(sample_text))