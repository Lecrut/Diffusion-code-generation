class WordCounter:
    def __init__(self, text):
        self.text = text

    def count_unique_words(self):
        words = self.text.split()
        unique_words = set(words)
        return len(unique_words)

if __name__ == '__main__':
    sample_text = "hello world hello Python"
    counter = WordCounter(sample_text)
    print(counter.count_unique_words())