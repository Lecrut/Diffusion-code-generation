import re

def count_vowels(text):
    pattern = r'[aeiouAEIOU]'
    matches = re.findall(pattern, text)
    return len(matches)

if __name__ == '__main__':
    test_string = "Hello World! This is a Test."
    result = count_vowels(test_string)
    print(result)