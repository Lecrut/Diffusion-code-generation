class StreamWordChecker:

    def __init__(self):
        self.seen_words = set()

    def process_chunk(self, chunk):
        for word in chunk.split():
            if word not in self.seen_words:
                print(f'New word found: {word}')
                self.seen_words.add(word)

def check_word_exists_in_stream(word, stream_chunks):
    checker = StreamWordChecker()
    for chunk in stream_chunks:
        checker.process_chunk(chunk)
    return word in checker.seen_words
if __name__ == '__main__':
    sample_stream_chunks = ['hello world', 'world peace', 'hello everyone']
    print(check_word_exists_in_stream('hello', sample_stream_chunks))
    print(check_word_exists_in_stream('goodbye', sample_stream_chunks))