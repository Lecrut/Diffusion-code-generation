class StreamWordChecker:
    def __init__(self):
        self.seen_words = set()
    
    def process_chunk(self, chunk: str) -> None:
        words = chunk.split()
        for word in words:
            if word not in self.seen_words:
                print(f'New word found: {word}')
                self.seen_words.add(word)
    
    def check_word_exists(self, word: str) -> bool:
        return word in self.seen_words

if __name__ == '__main__':
    checker = StreamWordChecker()
    chunks = ['python programming', 'programming is fun', 'fun with python']
    for chunk in chunks:
        checker.process_chunk(chunk)
    print(checker.check_word_exists('python'))
    print(checker.check_word_exists('java'))