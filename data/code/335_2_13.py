class SentenceSplitter:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if len(word) > 1]
if __name__ == '__main__':
    splitter = SentenceSplitter()
    input_text = "Hello   world! This is a test."
    result = splitter.split_sentence(input_text)
    print(result)