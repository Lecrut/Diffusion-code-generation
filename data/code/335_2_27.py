class SentenceSplitter:
    def split_sentence(self, sentence):
        return [word.strip() for word in sentence.split()]
if __name__ == '__main__':
    splitter = SentenceSplitter()
    input_text = "  Hello   world. This is a test."
    result = splitter.split_sentence(input_text)
    print(result)