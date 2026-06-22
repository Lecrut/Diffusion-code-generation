import re

def remove_vowels(text):
    pattern = re.compile(r'[aeiouAEIOU]')
    return pattern.sub('', text)

if __name__ == '__main__':
    sample_input = "Hello World! This is an Example."
    result = remove_vowels(sample_input)
    print(result)