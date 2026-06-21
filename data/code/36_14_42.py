class SentenceReverser:
    def __init__(self, sentence):
        self.sentence = sentence

    @staticmethod
    def reverse_words(words):
        return words[::-1]

    def reverse_sentence(self):
        words = self.sentence.split()
        reversed_words = self.reverse_words(words)
        return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Implementing a unique solution"
    reverser = SentenceReverser(sample_sentence)
    print(reverser.reverse_sentence())