class WordDictionary:
    def __init__(self):
        self.word_set = set()
    def add_word(self, word):
        if word and word not in self.word_set:
            self.word_set.add(word)
if __name__ == '__main__':
    wd = WordDictionary()
    words_to_add = ["apple", "banana", "apple", "", "cherry", "banana"]
    for word in words_to_add:
        wd.add_word(word)
    print(list(wd.word_set))