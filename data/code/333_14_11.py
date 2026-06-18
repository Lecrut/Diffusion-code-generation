import re
def extract_initial_chars(text: str) -> str:
    words = text.split()
    if not words:
        return ""
    initials = []
    for word in words:
        match = re.match(r'\S', word)
        if match:
            initials.append(match.group())
    return ''.join(initials)
if __name__ == '__main__':
    sample_text = "Hello world! Python is awesome. How are you?"
    result = extract_initial_chars(sample_text)
    print(result)