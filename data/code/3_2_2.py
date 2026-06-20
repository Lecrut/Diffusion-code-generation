import re

def filter_vowels(text):
    pattern = r'[aeiouAEIOU]'
    return re.sub(pattern, '', text)

if __name__ == '__main__':
    sample_string = "Hello World, this is a Test String!"
    result = filter_vowels(sample_string)
    print(result)