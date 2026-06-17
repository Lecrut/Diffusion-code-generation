import re
def get_initial_chars(text: str) -> str:
    matches = re.findall(r'\b\w', text)
    return ''.join(matches) if matches else ''
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string for the algorithm."
    result = get_initial_chars(sample_string)
    print(result)