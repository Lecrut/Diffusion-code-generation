import re
def get_initial_chars(text: str) -> str:
    matches = re.findall(r'\b\w', text, flags=re.UNICODE)
    if not matches:
        return ""
    result_chars = [match[0] for match in matches]
    return ''.join(result_chars)
if __name__ == '__main__':
    sample_string = "Hello World! This is a test string with multiple words."
    output = get_initial_chars(sample_string)
    print(output)