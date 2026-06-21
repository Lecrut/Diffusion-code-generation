import re

def find_first_letter(text):
    pattern = re.compile(r'[a-zA-Z]')
    match = pattern.search(text)
    return match.group(0) if match else None

if __name__ == '__main__':
    test_cases = [
        "42 is the answer",
        "!@#",
        "Hello, World!",
        "",
        "123abc"
    ]
    for case in test_cases:
        first_letter = find_first_letter(case)
        print(first_letter)