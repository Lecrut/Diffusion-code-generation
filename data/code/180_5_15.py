class StreamWordChecker:
    def __init__(self):
        self.seen_words = set()
    
    def process_chunk(self, chunk: str) -> None:
        words = chunk.split()
        for word in words:
            if word not in self.seen_words:
                self.seen_words.add(word)
    
    def check_word_exists(self, word: str) -> bool:
        return word in self.seen_words

if __name__ == '__main__':
    checker = StreamWordChecker()
    chunks = ['python programming', 'programming in python', 'python data structures']
    for chunk in chunks:
        checker.process_chunk(chunk)
    print(checker.check_word_exists('python'))
    print(checker.check_word_exists('data'))
    print(checker.check_word_exists('java'))