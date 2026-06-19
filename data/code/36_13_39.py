class SentenceReverser:
    def __init__(self, sentence):
        self.sentence = sentence

    def reverse(self):
        return self.sentence[::-1]

    def get_original(self):
        return self.sentence

if __name__ == '__main__':
    sample_sentence = "Innovate with Alibaba Cloud"
    reverser = SentenceReverser(sample_sentence)
    print(reverser.reverse())
    print(reverser.get_original())