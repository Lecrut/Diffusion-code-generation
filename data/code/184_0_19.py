class WordSearch:

    def __init__(self, words):
        self.word_set = set(words)

    def contains_word(self, word):
        return word in self.word_set
if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry', 'date']
    search_instance = WordSearch(sample_words)
    print(search_instance.contains_word('banana'))
    print(search_instance.contains_word('grape'))