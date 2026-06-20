import re

def find_first_letter(text):
    match = re.search(r'[a-zA-Z]', text)
    if match:
        return match.group(0)
    return None

if __name__ == '__main__':
    samples = [
        "123 abc",
        "",
        "123!@#",
        "Hello World",
        "   leading spaces then A"
    ]
    for sample in samples:
        print(find_first_letter(sample))