class StringProcessor:
    def __init__(self, text):
        self.text = text

    def split_into_words(self):
        return self.text.split()

if __name__ == '__main__':
    processor = StringProcessor('Python is awesome')
    words = processor.split_into_words()
    print(words)