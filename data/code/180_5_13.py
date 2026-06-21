class StreamWordChecker:
    def __init__(self):
        self.seen_words = set()

    @staticmethod
    def process_chunk(chunk: str, seen_words: set) -> None:
        words = chunk.split()
        for word in words:
            if word not in seen_words:
                print(f'New word found: {word}')
                seen_words.add(word)

    def check_word_exists(self, word: str) -> bool:
        return word in self.seen_words

if __name__ == '__main__':
    checker = StreamWordChecker()
    chunks = ['hello world', 'world hello', 'hello universe']
    for chunk in chunks:
        StreamWordChecker.process_chunk(chunk, checker.seen_words)
    print(checker.check_word_exists('hello'))
    print(checker.check_word_exists('universe'))