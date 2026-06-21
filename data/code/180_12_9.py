class WordSearcher:

    def __init__(self, word_list):
        self.word_set = {w.lower() for w in word_list}

    def contains_word(self, word):
        return word.lower() in self.word_set
if __name__ == '__main__':
    searcher = WordSearcher(['java', 'c++', 'python', 'ruby'])
    print(searcher.contains_word('Python'))
    print(searcher.contains_word('Java'))
    print(searcher.contains_word('c++'))
    print(searcher.contains_word('Ruby'))
    print(searcher.contains_word('Go'))