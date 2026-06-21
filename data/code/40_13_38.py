import re

def find_first_letter(text):
    match = re.search(r'[a-zA-Z]', text)
    return match.group(0) if match else None

if __name__ == '__main__':
    sample_values = [
        "123abc",
        "!@#",
        "Hello, World!",
        "",
        "42 is the answer"
    ]
    
    for value in sample_values:
        result = find_first_letter(value)
        print(result)