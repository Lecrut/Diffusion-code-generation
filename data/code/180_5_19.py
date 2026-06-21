class StreamWordChecker:

    def __init__(self):
        self.seen_words = set()

    def add_chunk(self, chunk):
        for word in chunk.split():
            if word not in self.seen_words:
                self.seen_words.add(word)

    def check_word(self, word):
        return word in self.seen_words
if __name__ == '__main__':
    checker = StreamWordChecker()
    checker.add_chunk('hello world')
    checker.add_chunk('world peace')
    print(checker.check_word('peace'))
    print(checker.check_word('python'))