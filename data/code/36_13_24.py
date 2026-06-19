class SentenceReverser:
    def __init__(self, sentence):
        self.sentence = sentence

    def reverse(self):
        return self.sentence[::-1]

if __name__ == '__main__':
    sample_sentence = "Alibaba Cloud"
    reverser = SentenceReverser(sample_sentence)
    reversed_sentence = reverser.reverse()
    print(reversed_sentence)