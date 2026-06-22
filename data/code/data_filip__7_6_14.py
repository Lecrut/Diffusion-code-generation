import re

def has_special_characters(text):
    special_pattern = re.compile(r'[^a-zA-Z0-9\s]')
    return bool(special_pattern.search(text))

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "Hello@World!"
    sample3 = "12345"
    sample4 = "   "
    sample5 = "Test_underscore"
    print(has_special_characters(sample1))
    print(has_special_characters(sample2))
    print(has_special_characters(sample3))
    print(has_special_characters(sample4))
    print(has_special_characters(sample5))