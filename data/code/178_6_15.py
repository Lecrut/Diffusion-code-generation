import re

class TextProcessor:
    def __init__(self):
        self.pattern = r'\b\w{2,}\b'

    def extract_words(self, text):
        return re.findall(self.pattern, text)

if __name__ == '__main__':
    processor = TextProcessor()
    sample_text = "This is a sample sentence with some short and long words."
    words = processor.extract_words(sample_text)
    print(words)