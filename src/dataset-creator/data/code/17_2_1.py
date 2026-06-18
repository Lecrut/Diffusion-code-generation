class WordDictionary:
    def __init__(self):
        self.word_counts = {}
    def load_text(self, text):
        words = text.lower().split()
        for word in words:
            if word:
                self.word_counts[word] = self.word_counts.get(word, 0) + 1
    def get_word_frequencies(self):
        return self.word_counts
if __name__ == '__main__':
    text_data = "The quick brown fox jumps over the lazy dog. Fox and dog are friends."
    word_dict = WordDictionary()
    word_dict.load_text(text_data)
    frequencies = word_dict.get_word_frequencies()
    print(frequencies)