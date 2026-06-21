class WordIndexer:
    def __init__(self, words):
        self.words = words
        self.indices = sorted(range(len(words)), key=lambda x: len(words[x]))
    
    def generate_word_dict(self):
        return {i: self.words[idx] for idx, i in enumerate(self.indices)}

if __name__ == '__main__':
    indexer = WordIndexer(["apple", "banana", "cherry"])
    print(indexer.generate_word_dict())