import re

def remove_vowels(text):
    return re.sub(r'[aeiouAEIOU]', '', text)

if __name__ == '__main__':
    sample_string = "Hello World"
    result = remove_vowels(sample_string)
    print(result)