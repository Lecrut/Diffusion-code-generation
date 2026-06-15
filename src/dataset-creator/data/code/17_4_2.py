class WordDictionary:
    def __init__(self):
        self.frequency = {}
    def process_string(self, text):
        words = text.split()
        for word in words:
            self.frequency[word] = self.frequency.get(word, 0) + 1
if __name__ == '__main__':
    word_dict = WordDictionary()
    sample_string = "apple banana apple orange banana apple"
    word_dict.process_string(sample_string)
    print(word_dict.frequency)