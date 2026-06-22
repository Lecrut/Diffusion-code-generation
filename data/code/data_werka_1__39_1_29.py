import re

def validate_pattern(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

def extract_all_non_overlapping(text, pattern):
    if not validate_pattern(pattern):
        raise ValueError("Invalid regular expression pattern")
    return re.findall(pattern, text)

if __name__ == '__main__':
    input_string = "hello world hello universe hello galaxy"
    pattern = r"\bhello\b"
    result = extract_all_non_overlapping(input_string, pattern)
    print(result)