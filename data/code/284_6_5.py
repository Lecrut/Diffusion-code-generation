class SentenceReverser:
    def reverse_words(self, sentence):
        return ' '.join(sentence.split()[::-1])

if __name__ == '__main__':
    reverser = SentenceReverser()
    sample_sentence = "Hello world from Python"
    reversed_sentence = reverser.reverse_words(sample_sentence)
    print(reversed_sentence)