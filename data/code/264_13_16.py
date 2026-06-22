class WordCounter:
    def __init__(self):
        self.word_count = {}

    def count_words(self, text):
        words = text.split()
        for word in words:
            self.word_count[word] = self.word_count.get(word, 0) + 1

    def get_most_frequent_word(self):
        return max(self.word_count.items(), key=lambda x: x[1])

if __name__ == '__main__':
    counter = WordCounter()
    sample_text = "hello world hello python programming is fun and exciting"
    counter.count_words(sample_text)
    most_frequent, count = counter.get_most_frequent_word()
    print(f"The most frequent word is '{most_frequent}' with a count of {count}")