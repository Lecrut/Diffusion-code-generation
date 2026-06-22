class TextProcessor:
    def __init__(self, text):
        self.text = text

    def count_unique_words(self):
        words = self.text.split()
        unique_words = set(words)
        return len(unique_words)

if __name__ == '__main__':
    processor = TextProcessor("hello world hello Python")
    print(processor.count_unique_words())