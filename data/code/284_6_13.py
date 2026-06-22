class SentenceReverser:
    DEFAULT_SEPARATOR = ' '

    @staticmethod
    def reverse_words(sentence):
        words = sentence.split(SentenceReverser.DEFAULT_SEPARATOR)
        reversed_words = [word[::-1] for word in words]
        return SentenceReverser.DEFAULT_SEPARATOR.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    reversed_sentence = SentenceReverser.reverse_words(sample_sentence)
    print(reversed_sentence)