import re

def remove_vowels(text):
    return re.sub(r'[aeiouAEIOU]', '', text)

if __name__ == '__main__':
    print(remove_vowels("Hello, World!"))
    print(remove_vowels("Python Programming"))