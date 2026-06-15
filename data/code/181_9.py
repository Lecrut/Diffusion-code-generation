import re
def filter_vowels(text):
    return re.sub(r'[^aeiouAEIOU]', '', text)
if __name__ == '__main__':
    sample_string = "Hello World! This is a test string."
    result = filter_vowels(sample_string)
    print(result)