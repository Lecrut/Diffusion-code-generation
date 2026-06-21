class WordFinder:

    def __init__(self, word_list):
        self.lowercased_words = set((word.lower() for word in word_list))

    def contains_word(self, word):
        return word.lower() in self.lowercased_words
if __name__ == '__main__':
    sample_list = ['java', 'c++', 'python', 'ruby']
    finder = WordFinder(sample_list)
    print(finder.contains_word('Python'))
    print(finder.contains_word('java'))
    print(finder.contains_word('JavaScript'))