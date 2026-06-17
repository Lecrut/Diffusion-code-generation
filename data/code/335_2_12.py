class SentenceSplitter:
    def split(self, sentence):
        return [word for word in sentence.split() if len(word) > 1]
if __name__ == '__main__':
    splitter = SentenceSplitter()
    test_sentence = "Hello   world! This is a   test."
    result = splitter.split(test_sentence.lower().replace("!", ""))
    print(result)