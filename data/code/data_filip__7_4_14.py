import re

def get_first_special_char(text):
    pattern = re.compile(r'[^a-zA-Z0-9\s]')
    match = pattern.search(text)
    if match:
        return match.group(0)
    return None

if __name__ == '__main__':
    sample_strings = ["Hello World", "Hello@World", "NoSpecialHere123"]
    for s in sample_strings:
        result = get_first_special_char(s)
        print(result)