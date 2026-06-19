import re

def find_first_letter(text):
    match = re.search(r'[a-zA-Z]', text)
    return match.group(0) if match else None

if __name__ == '__main__':
    sample_values = [
        "Hello, World!",
        "123456",
        "!@#$%^&*()",
        "",
        "Python3.8"
    ]
    
    for value in sample_values:
        result = find_first_letter(value)
        print(result)