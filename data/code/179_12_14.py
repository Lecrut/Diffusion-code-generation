class SentenceReverser:
    def reverse_words(self, sentence):
        words = sentence.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

if __name__ == '__main__':
    reverser = SentenceReverser()
    sample_sentence = "Hello world from Python"
    reversed_sentence = reverser.reverse_words(sample_sentence)
    print(reversed_sentence)