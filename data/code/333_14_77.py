import re
def get_initial_chars(text: str) -> str:
    matches = re.findall(r'\b\w+\b', text.lower())
    if not matches:
        return ""
    initial_chars = [word[0] for word in matches]
    return ''.join(initial_chars)
if __name__ == '__main__':
    sample_text = "Hello World! This is a test string. Python 3.12 is great."
    result = get_initial_chars(sample_text)
    print(result)