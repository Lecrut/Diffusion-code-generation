class StreamWordChecker:
    def __init__(self):
        self.seen_words = set()

    def add_chunk(self, chunk):
        words = chunk.split()
        for word in words:
            if word not in self.seen_words:
                print(f"New word found: {word}")
                self.seen_words.add(word)

def check_word_exists(stream_data, target_word):
    checker = StreamWordChecker()
    for chunk in stream_data:
        checker.add_chunk(chunk)
    return target_word in checker.seen_words

if __name__ == '__main__':
    stream_data = [
        "hello world",
        "world is beautiful",
        "hello everyone"
    ]
    target_word = "everyone"
    print(check_word_exists(stream_data, target_word))