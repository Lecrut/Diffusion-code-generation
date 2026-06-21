class TextProcessor:
    def __init__(self, text):
        self.text = text

    def split_into_words(self):
        return [word for word in self.text.split(' ') if word]

if __name__ == '__main__':
    processor = TextProcessor("  multiple   spaces  between  words  ")
    words = processor.split_into_words()
    print(words)