import re

def count_vowels(text):
    return len(re.findall(r'[aeiouAEIOU]', text))

if __name__ == '__main__':
    test_string = "Hello World"
    print(count_vowels(test_string))