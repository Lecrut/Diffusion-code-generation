import re
def get_initial_chars(text: str) -> str:
    if not text.strip():
        return ""
    matches = re.findall(r'\b\w', text, flags=re.UNICODE)
    result_chars = [match[0] for match in matches if len(match) > 0]
    return ''.join(result_chars)
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string with multiple words."
    output = get_initial_chars(sample_string)
    print(output)