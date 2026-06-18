class SentenceSplitter:
    def split(self, sentence):
        return [word for word in sentence.split() if len(word) > 1]
if __name__ == '__main__':
    splitter = SentenceSplitter()
    test_sentence = "Hello   world! Python is great."
    result = splitter.split(test_sentence.lower())
    print(result)