class TextProcessor:
    def __init__(self, text):
        self.text = text

    def split_text(self):
        return self.text.split()

if __name__ == '__main__':
    sample_text = "Hello world this is a test"
    processor = TextProcessor(sample_text)
    words = processor.split_text()
    print(words)