import re
def get_initial_chars(text: str) -> str:
    words = text.split()
    if not words:
        return ""
    result_parts = []
    for word in words:
        match = re.match(r'\S', word)
        if match:
            result_parts.append(match.group())
    return "".join(result_parts)
if __name__ == '__main__':
    sample_text = "Hello world! Python is great. Regular expressions are powerful."
    output = get_initial_chars(sample_text)
    print(output)