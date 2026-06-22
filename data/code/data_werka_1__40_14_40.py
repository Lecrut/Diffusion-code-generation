import re

class TextAnalyzer:
    ALPHABET_PATTERN = re.compile(r'[a-zA-Z]')

    @staticmethod
    def find_first_letter(text):
        match = TextAnalyzer.ALPHABET_PATTERN.search(text)
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
        print(TextAnalyzer.find_first_letter(text))