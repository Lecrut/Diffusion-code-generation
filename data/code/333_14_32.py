import re
def get_initial_chars(text: str) -> str:
    matches = re.findall(r'\b\w', text, flags=re.UNICODE)
    if not matches:
        return ""
    result_chars = [char for char in matches]
    return ''.join(result_chars)
if __name__ == '__main__':
    sample_string = "Hello world! This is a test string. Python 3.10."
    output = get_initial_chars(sample_string)
    print(output)