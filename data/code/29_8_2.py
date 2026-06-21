import re

def count_vowels(text):
    pattern = r'[aeiouAEIOU]'
    return len(re.findall(pattern, text))

if __name__ == '__main__':
    test_string = "Hello, World! This is a hard-coded test string."
    result = count_vowels(test_string)
    print(result)