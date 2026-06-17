import re
def get_initial_chars(text: str) -> str:
    matches = re.findall(r'\b\w', text, flags=re.UNICODE)
    if not matches:
        return ""
    result_chars = [match[0] for match in matches]
    return ''.join(result_chars)
if __name__ == '__main':
    sample_text = "Hello World! Python is great. Regular expressions are powerful."
    output = get_initial_chars(sample_text)
    print(output)

if __name__ == '__main__':
    pass
