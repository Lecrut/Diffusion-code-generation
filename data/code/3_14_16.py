import re

_vowel_pattern = re.compile(r'[aeiouAEIOU]')

def _validate_input(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text

def remove_vowels(text):
    _validate_input(text)
    return _vowel_pattern.sub('', text)

if __name__ == '__main__':
    samples = [
        "Hello World",
        "Python Programming",
        "AEIOU",
        "xyz",
        "Remove all vowels from this string"
    ]
    for sample in samples:
        result = remove_vowels(sample)
        print(result)