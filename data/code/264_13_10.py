class WordCounter:
    def __init__(self):
        self.word_count = {}

    def update(self, text):
        words = text.split()
        for word in words:
            self.word_count[word] = self.word_count.get(word, 0) + 1

    def most_frequent_word(self):
        return max(self.word_count.items(), key=lambda x: x[1])

if __name__ == '__main__':
    sample_text = "hello world hello python programming is fun and exciting"
    counter = WordCounter()
    counter.update(sample_text)
    most_frequent, count = counter.most_frequent_word()
    print(f"The most frequent word is '{most_frequent}' with a count of {count}")