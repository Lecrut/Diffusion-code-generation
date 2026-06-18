import re
def get_initial_chars(text: str) -> str:
    matches = re.findall(r'\b\w', text, flags=re.UNICODE)
    if not matches:
        return ""
    result_chars = [m[0] for m in matches]
    return ''.join(result_chars)
if __name__ == '__main':
    sample_string = "Hello world! This is a test string with multiple words."
    output = get_initial_chars(sample_string)
    print(output)

if __name__ == '__main__':
    pass
