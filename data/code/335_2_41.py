class SentenceSplitter:
    def split(self, sentence):
        return [word for word in sentence.split() if len(word.strip()) > 0]
if __name__ == '__main__':
    splitter = SentenceSplitter()
    test_sentence = "Hello   World! This is a      test."
    result = splitter.split(test_sentence)
    print(result)