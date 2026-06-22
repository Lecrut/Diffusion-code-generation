class SentenceReverser:
    DELIMITER = ' '

    @staticmethod
    def reverse_words(sentence):
        return SentenceReverser.DELIMITER.join(reversed(sentence.split()))

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    reversed_sentence = SentenceReverser.reverse_words(sample_sentence)
    print(reversed_sentence)