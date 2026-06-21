import re

class WordSplitter:
    def __init__(self):
        self.pattern = r'\W+'

    def split_text(self, text):
        return [word for word in re.split(self.pattern, text) if word]

if __name__ == '__main__':
    splitter = WordSplitter()
    sample_text = "Hello, world! This is a test. Multiple   spaces and punctuation... should work."
    words = splitter.split_text(sample_text)
    print(words)