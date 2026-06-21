class SentenceSplitter:
    @staticmethod
    def split(sentence):
        return sentence.split()

if __name__ == '__main__':
    sample_sentence = "  Hello   world! This is a test sentence. "
    splitter = SentenceSplitter()
    words = splitter.split(sample_sentence)
    print(words)