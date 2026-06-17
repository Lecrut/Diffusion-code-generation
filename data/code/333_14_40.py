import re
def get_initial_chars(text: str) -> str:
    if not text.strip():
        return ""
    matches = re.findall(r'\w+', text.lower())
    if not matches:
        return ""
    initials = [match[0] for match in matches]
    return ''.join(initials).upper()
if __name__ == '__main__':
    sample_text = "Hello world! This is a test string. Python 3.9 is great."
    result = get_initial_chars(sample_text)
    print(result)