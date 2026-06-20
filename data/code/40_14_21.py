import re

def find_first_letter(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if not text:
        return None
    match = re.search(r'[a-zA-Z]', text)
    return match.group(0) if match else None

if __name__ == '__main__':
    sample_texts = ["12345", "!@#$%", "   789abc", "Hello World", ""]
    for s in sample_texts:
        print(find_first_letter(s))