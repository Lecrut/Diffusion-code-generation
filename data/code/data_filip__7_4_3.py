import re

def get_first_special_char(text):
    special_pattern = re.compile(r'[^a-zA-Z0-9\s]')
    match = special_pattern.search(text)
    if match:
        return match.group()
    return None

if __name__ == '__main__':
    sample_text = "Hello World! 123"
    result = get_first_special_char(sample_text)
    print(result)