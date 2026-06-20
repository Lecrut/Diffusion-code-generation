import re

def remove_vowels(text):
    pattern = re.compile(r'[aeiouAEIOU]')
    return pattern.sub('', text)

if __name__ == '__main__':
    sample_string = "Hello World! This is an example string."
    result = remove_vowels(sample_string)
    print(result)