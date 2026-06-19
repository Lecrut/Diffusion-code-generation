import re

class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def find_first_letter(self):
        if not isinstance(self.text, str):
            raise ValueError("Input must be a string")
        match = re.search(r'[a-zA-Z]', self.text)
        return match.group(0) if match else None

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
        analyzer = TextAnalyzer(text)
        result = analyzer.find_first_letter()
        print(f"First letter in '{text}': {result}")