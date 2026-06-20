import re

def strip_vowels(text):
    return re.sub(r'[aeiouAEIOU]', '', text)

if __name__ == '__main__':
    print(strip_vowels("Hello World"))