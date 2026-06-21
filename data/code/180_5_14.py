class StreamWordChecker:

    def __init__(self):
        self.seen_words = set()

    def process_chunk(self, chunk):
        words = chunk.split()
        for word in words:
            if word not in self.seen_words:
                self.seen_words.add(word)

    def check_word(self, word):
        return word in self.seen_words
if __name__ == '__main__':
    checker = StreamWordChecker()
    checker.process_chunk('hello world')
    checker.process_chunk('world hello universe')
    print(checker.check_word('hello'))
    print(checker.check_word('universe'))
    print(checker.check_word('python'))