import re

def find_first_letter(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    match = re.search(r'[a-zA-Z]', text)
    return match.group(0) if match else None

class TextProcessor:
    def __init__(self, text):
        self.text = text
    
    def get_first_letter(self):
        return find_first_letter(self.text)

if __name__ == '__main__':
    sample_values = [
        "123abc",
        "!@#",
        "Hello, World!",
        "",
        "42 is the answer"
    ]
    
    for value in sample_values:
        processor = TextProcessor(value)
        print(processor.get_first_letter())