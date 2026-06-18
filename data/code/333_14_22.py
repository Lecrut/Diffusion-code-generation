import re
def extract_initials(text: str) -> str:
    pattern = r'\b[a-zA-Z][a-zA-Z]*\b'
    matches = re.findall(pattern, text)
    return ''.join(match[0].upper() for match in matches if len(match) > 1 or any(c.isalpha() and not c.isdigit() for c in match))
if __name__ == '__main__':
    sample_text = "Hello World! This is a test string."
    result = extract_initials(sample_text)
    print(result)