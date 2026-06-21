class WordSearcher:
    def __init__(self, word_list):
        self.lowercased_words = set(w.lower() for w in word_list)

    @staticmethod
    def create_from_list(word_list):
        return WordSearcher(word_list)

    def contains_word(self, word):
        return word.lower() in self.lowercased_words

if __name__ == '__main__':
    sample_word = 'Python'
    sample_list = ['java', 'c++', 'python', 'ruby']
    searcher = WordSearcher.create_from_list(sample_list)
    print(searcher.contains_word(sample_word))