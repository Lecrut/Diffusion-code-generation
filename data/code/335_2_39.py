class SentenceSplitter:
    def split(self, sentence):
        return [word.strip() for word in sentence.split()]
if __name__ == '__main__':
    splitter = SentenceSplitter()
    sample_sentence = "  Hello   world, this is a test.  "
    result = splitter.split(sample_sentence)
    print(result)