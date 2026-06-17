class SentenceSplitter:
    def split(self, sentence):
        return sentence.split()
if __name__ == '__main__':
    splitter = SentenceSplitter()
    test_sentence = "Hello   world  this is a test"
    result = splitter.split(test_sentence)
    print(result)