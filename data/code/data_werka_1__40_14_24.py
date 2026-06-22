import re

def find_first_letter(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    match = re.search(r'[a-zA-Z]', text)
    if match:
        return match.group(0)
    else:
        return None

if __name__ == '__main__':
    sample_texts = [
        'Hello, World!',
        '1234567890',
        '',
        '!@#$%^&*()',
        'Python3.8',
        'no letters here',
        '1st letter'
    ]
    
    for text in sample_texts:
        try:
            result = find_first_letter(text)
            print(f"First letter in '{text}': {result}")
        except ValueError as e:
            print(e)