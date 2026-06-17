import re
def extract_initials(text: str) -> str:
    matches = re.findall(r'\b[A-Za-z]\w*', text)
    return ''.join(match[0] for match in matches if len(match) > 1 and not (len(match) == 2)) or ''
if __name__ == '__main__':
    sample_text = "Hello World, Python Programming is Fun!"
    result = extract_initials(sample_text)
    print(result)