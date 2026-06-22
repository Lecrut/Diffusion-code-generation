class WordProcessor:
    def __init__(self):
        self.longest_word = ""
        self.max_length = 0

    def update_longest_word(self, word):
        if len(word) > self.max_length:
            self.longest_word = word
            self.max_length = len(word)

    def find_longest_word(self, words):
        for word in words:
            self.update_longest_word(word)
        return self.longest_word, self.max_length

if __name__ == '__main__':
    processor = WordProcessor()
    sample_words = ["apple", "banana", "cherry", "date"]
    result = processor.find_longest_word(sample_words)
    print(f"Longest word: {result[0]}, Length: {result[1]}")