class WordCounter:
    def count_words(self, text):
        words = text.split()
        return len(words)

if __name__ == '__main__':
    sample_text = "Hello world this is a test"
    counter = WordCounter()
    print(counter.count_words(sample_text))