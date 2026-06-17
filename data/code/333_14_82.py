import re
def get_initial_chars(s):
    matches = re.findall(r'\b\w', s)
    return ''.join(matches) if matches else ''
if __name__ == '__main':
    sample_string = "Hello, world! This is a test string for processing."
    result = get_initial_chars(sample_string)
    print(result)

if __name__ == '__main__':
    pass
