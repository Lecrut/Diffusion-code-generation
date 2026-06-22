class TextProcessor:
    def __init__(self, text):
        self.text = text

    def get_text_length(self):
        return len(self.text)

    def is_empty(self):
        return len(self.text) == 0

if __name__ == '__main__':
    sample_text = "Hello, World!"
    processor = TextProcessor(sample_text)
    print(processor.get_text_length())
    print(processor.is_empty())