class WordCounter:
    @staticmethod
    def count_words(text):
        words = text.split()
        return len(words)

if __name__ == '__main__':
    sample_text = "Hello world this is a test"
    word_count = WordCounter.count_words(sample_text)
    print(word_count)