import re
def get_first_letters(s):
    matches = re.findall(r'\b\w', s)
    return ''.join(matches[:1] if len(matches) > 0 else '') or ''
if __name__ == '__main__':
    sample_string = "Hello World! This is a test string for regex."
    result = get_first_letters(sample_string)
    print(result)