class WordSearcher:

    def __init__(self, word_list):
        self.word_set = set((w.lower() for w in word_list))

    def is_word_present(self, word):
        return word.lower() in self.word_set
if __name__ == '__main__':
    searcher = WordSearcher(['java', 'c++', 'python', 'ruby'])
    print(searcher.is_word_present('Python'))
    print(searcher.is_word_present('c++'))
    print(searcher.is_word_present('javascript'))