class WordFinder:
    def __init__(self, words):
        self.words = words

    def find_first_word(self):
        return self.words.split()[0]

if __name__ == '__main__':
    sample_words = "Hello   world from Qwen"
    finder = WordFinder(sample_words)
    print(finder.find_first_word())