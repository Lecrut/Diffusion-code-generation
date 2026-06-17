class SentenceSplitter:
    def split(self, sentence):
        return [word.strip() for word in sentence.split()]
if __name__ == '__main__':
    splitter = SentenceSplitter()
    test_sentence = "Hello   world  This is a test."
    result = splitter.split(test_sentence)
    print(result)