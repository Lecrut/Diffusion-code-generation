import re

def remove_vowels(text):
    pattern = r'[aeiouAEIOU]'
    return re.sub(pattern, '', text)

if __name__ == '__main__':
    sample_string = "Hello World, this is a Test string with Vowels!"
    result = remove_vowels(sample_string)
    print(result)