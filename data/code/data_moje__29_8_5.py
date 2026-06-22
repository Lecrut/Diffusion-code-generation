import re

def count_vowels(text):
    return len(re.findall(r'[aeiouAEIOU]', text))

if __name__ == '__main__':
    test_string = "Hello World! This is a hard-coded test string for counting vowels."
    result = count_vowels(test_string)
    print(result)