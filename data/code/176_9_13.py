import re

class TextProcessor:
    def __init__(self, text):
        self.text = text

    def extract_letter_sequences(self):
        return re.findall(r'\b[a-zA-Z]+\b', self.text)

if __name__ == '__main__':
    sample_text = "Hello, World! 123 Python 3.8"
    processor = TextProcessor(sample_text)
    print(processor.extract_letter_sequences())