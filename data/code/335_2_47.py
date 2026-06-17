class SentenceSplitter:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if word]
if __name__ == '__main__':
    splitter = SentenceSplitter()
    sample_input = "  Hello   world  and   Python.  "
    result = splitter.split_sentence(sample_input)
    print(result)