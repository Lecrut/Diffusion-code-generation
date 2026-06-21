class WordSearcher:
    @staticmethod
    def is_word_in_collection(word, collection):
        return any(word == item for item in collection)

if __name__ == '__main__':
    searcher = WordSearcher()
    sample_word = 'hello'
    sample_collection = ['world', 'python', 'hello', 'programming']
    print(searcher.is_word_in_collection(sample_word, sample_collection))