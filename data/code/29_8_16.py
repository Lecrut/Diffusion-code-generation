import re

def count_vowels(text):
    pattern = r'[aeiouAEIOU]'
    matches = re.findall(pattern, text)
    return len(matches)

if __name__ == '__main__':
    test_string = "Hello World, this is a test string with vowels."
    result = count_vowels(test_string)
    print(result)