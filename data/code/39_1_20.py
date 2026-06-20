import re

def extract_pattern(input_string: str, pattern: str) -> list:
    compiled_pattern = re.compile(pattern)
    return compiled_pattern.findall(input_string)
if __name__ == '__main__':
    text = 'The rain in Spain falls mainly in the plain.'
    regex_pattern = '\\b\\w{4}\\b'
    results = extract_pattern(text, regex_pattern)
    print(results)