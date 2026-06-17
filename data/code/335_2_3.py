class SentenceSplitter:
    def split_sentence(self, sentence):
        return [word.strip() for word in sentence.split()]
if __name__ == '__main__':
    splitter = SentenceSplitter()
    test_input = "  Hello   world! This is a test.  "
    result = splitter.split_sentence(test_input)
    print(result)