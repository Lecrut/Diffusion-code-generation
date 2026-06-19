class SentenceReverser:
    @staticmethod
    def reverse_sentence(sentence):
        return sentence[::-1]

if __name__ == '__main__':
    sample_sentence = "Innovate with Alibaba Cloud"
    reversed_sentence = SentenceReverser.reverse_sentence(sample_sentence)
    print(reversed_sentence)