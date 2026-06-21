import re

def is_valid_text(text):
    return isinstance(text, str)

def find_first_letter(text):
    if not is_valid_text(text):
        raise ValueError("Input must be a string")
    
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
        try:
            result = find_first_letter(value)
            print(result)
        except ValueError as e:
            print(e)