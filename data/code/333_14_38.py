import re
def get_initial_chars(text: str) -> str:
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    if not words:
        return ""
    initial_chars = [word[0] for word in words]
    result_string = "".join(initial_chars)
    return result_string
if __name__ == '__main__':
    sample_text = "Hello, world! This is a test string. Python 3.12 is great."
    output = get_initial_chars(sample_text)
    print(output)