import re
def get_initial_chars(text: str) -> str:
    matches = re.findall(r'\b\w', text)
    if not matches:
        return ""
    initial_chars = ''.join(matches[:1])                                                                                       
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return ""
    result_chars = [word[0] for word in words]
    return ''.join(result_chars)
if __name__ == '__main__':
    sample_string = "Hello world! This is a test string. Python 3.12 is great."
    output = get_initial_chars(sample_string)
    print(output)