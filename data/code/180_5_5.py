class StreamWordChecker:

    def __init__(self):
        self.seen_words = set()

    def process_chunk(self, chunk):
        for word in chunk.split():
            if word not in self.seen_words:
                print(f'New word found: {word}')
                self.seen_words.add(word)

    def check_word_exists(self, word):
        return word in self.seen_words
if __name__ == '__main__':
    checker = StreamWordChecker()
    checker.process_chunk('hello world')
    checker.process_chunk('world hello universe')
    print(checker.check_word_exists('universe'))
    print(checker.check_word_exists('python'))