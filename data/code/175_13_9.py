class SentenceSplitter:
    def split(self, sentence):
        return sentence.split()

if __name__ == '__main__':
    splitter = SentenceSplitter()
    sample_sentence = "  Hello   world!  This is a test sentence. "
    words = splitter.split(sample_sentence)
    print(words)