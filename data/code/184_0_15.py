class WordSearcher:

    def __init__(self, words):
        self.word_set = set(words)

    def contains_word(self, word):
        return word in self.word_set
if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry', 'date']
    searcher = WordSearcher(sample_words)
    print(searcher.contains_word('banana'))
    print(searcher.contains_word('grape'))