class TextSplitter:
    def __init__(self, text):
        self.text = text

    def split_words(self):
        return [word for word in self.text.split(' ') if word]

if __name__ == '__main__':
    splitter = TextSplitter("  multiple   spaces  between  words  ")
    words = splitter.split_words()
    print(words)