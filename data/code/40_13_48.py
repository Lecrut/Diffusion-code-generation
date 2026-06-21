import re

def find_first_letter(text):
    match = re.search(r'[a-zA-Z]', text)
    return match.group(0) if match else None

if __name__ == '__main__':
    sample_inputs = [
        "123abc",
        "!@#",
        "Hello World!",
        "",
        "42 is the answer"
    ]
    
    for input_text in sample_inputs:
        result = find_first_letter(input_text)
        print(f"First letter in '{input_text}': {result}")