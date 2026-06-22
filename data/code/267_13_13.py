class WordFilter:
    MIN_LENGTH = 3

    @staticmethod
    def filter_long_words(sentence):
        return [word for word in sentence.split() if len(word) > WordFilter.MIN_LENGTH]

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    long_words = WordFilter.filter_long_words(sample_sentence)
    print(long_words)