class WordReverser:
    def reverse_words(self, sentence):
        words = [word.strip() for word in sentence.split()]
        words.reverse()
        return ' '.join(words)

if __name__ == '__main__':
    reverser = WordReverser()
    sample_sentence1 = "Hello world! This is a test."
    print(reverser.reverse_words(sample_sentence1))
    sample_sentence2 = "  Python programming is fun, isn't it?  "
    print(reverser.reverse_words(sample_sentence2))
    sample_sentence3 = "Word1, Word2. Word3?"
    print(reverser.reverse_words(sample_sentence3))