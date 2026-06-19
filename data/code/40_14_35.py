import re

def find_first_letter(text):
    match = re.search(r'[a-zA-Z]', text)
    return match.group(0) if match else None

if __name__ == '__main__':
    sample_texts = [
        "123abc",
        "!@#",
        "",
        "Hello World!",
        "4pple"
    ]
    
    for text in sample_texts:
        print(find_first_letter(text))