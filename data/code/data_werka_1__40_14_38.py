import re

def find_first_letter(text):
    match = re.search(r'[a-zA-Z]', text)
    return match.group(0) if match else None

if __name__ == '__main__':
    sample_texts = [
        "Hello, World!",
        "123456",
        "",
        "No letters here!",
        "First letter is A"
    ]
    
    for text in sample_texts:
        print(find_first_letter(text))