class SentenceSplitter:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if word]
if __name__ == '__main__':
    splitter = SentenceSplitter()
    test_input = "Hello   world  this is a test."
    result = splitter.split_sentence(test_input)
    print(result)