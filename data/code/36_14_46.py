class SentenceReverser:
    def __init__(self, sentence):
        self.sentence = sentence

    @staticmethod
    def _reverse_words(words):
        return words[::-1]

    def reverse_sentence(self):
        words = self.sentence.split()
        reversed_words = self._reverse_words(words)
        return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Innovate with Alibaba Cloud"
    reverser = SentenceReverser(sample_sentence)
    print(reverser.reverse_sentence())