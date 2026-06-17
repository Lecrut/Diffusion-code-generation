class SentenceSplitter:
    def split_sentence(self, sentence):
        return sentence.split()
if __name__ == '__main__':
    splitter = SentenceSplitter()
    test_input = "  Hello   world  and Python . "
    result = splitter.split_sentence(test_input)
    print(result)