class WordIndexer:
    def __init__(self, words):
        self.words = words

    def generate_word_dict(self):
        indices = sorted(range(len(self.words)), key=lambda x: len(self.words[x]))
        word_dict = {i: self.words[idx] for i, idx in enumerate(indices)}
        return word_dict

if __name__ == '__main__':
    indexer = WordIndexer(["apple", "banana", "cherry"])
    print(indexer.generate_word_dict())