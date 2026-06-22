import re

def count_special_chars(s):
    special_pattern = re.compile(r'[^a-zA-Z0-9\s]')
    matches = special_pattern.findall(s)
    count = len(matches)
    status = count > 0
    return count, status

if __name__ == '__main__':
    sample_text = "Hello, World! 123"
    result = count_special_chars(sample_text)
    print(result)