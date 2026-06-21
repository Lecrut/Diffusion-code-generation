class CaseInsensitiveSearcher:

    def __init__(self):
        self.word_set = {'Python', 'Java', 'C++', 'ruby'}

    @staticmethod
    def to_lower(word):
        return word.lower()

    def match_word(self, word):
        return any((CaseInsensitiveSearcher.to_lower(w) == CaseInsensitiveSearcher.to_lower(word) for w in self.word_set))
if __name__ == '__main__':
    searcher = CaseInsensitiveSearcher()
    print(searcher.match_word('python'))
    print(searcher.match_word('java'))
    print(searcher.match_word('c++'))
    print(searcher.match_word('ruby'))
    print(searcher.match_word('perl'))