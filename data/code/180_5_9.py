class StreamWordChecker:

    def __init__(self):
        self.seen_words = set()

    def process_chunk(self, chunk):
        words = chunk.split()
        for word in words:
            if word not in self.seen_words:
                self.seen_words.add(word)

    def check_word_exists(self, word):
        return word in self.seen_words
if __name__ == '__main__':
    checker = StreamWordChecker()
    chunks = ['hello world', 'world peace', 'hello everyone']
    for chunk in chunks:
        checker.process_chunk(chunk)
    print(checker.check_word_exists('hello'))
    print(checker.check_word_exists('goodbye'))