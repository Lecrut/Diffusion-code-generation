import re
def extract_first_chars(text: str) -> str:
    pattern = r'\b\w'
    result = ''.join(match.group() for match in re.finditer(pattern, text))
    return result
if __name__ == '__main__':
    sample_text = "Hello World! This is a test string."
    output = extract_first_chars(sample_text)
    print(output)