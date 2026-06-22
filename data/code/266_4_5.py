class WordCounter:
    def __init__(self):
        self.unique_word_count = 0

    @staticmethod
    def count_unique_words(text):
        words = text.split()
        unique_words = set(words)
        return len(unique_words)

if __name__ == '__main__':
    sample_text = "hello world hello Python"
    counter = WordCounter()
    result = WordCounter.count_unique_words(sample_text)
    print(result)