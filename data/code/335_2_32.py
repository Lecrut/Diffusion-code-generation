class SentenceSplitter:
    def split(self, sentence):
        return [word for word in sentence.split() if word]
if __name__ == '__main__':
    splitter = SentenceSplitter()
    test_sentence = "Hello   world  this is a test"
    result = splitter.split(test_sentence)
    print(result)