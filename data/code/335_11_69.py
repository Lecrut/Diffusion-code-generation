class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if word]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_input = "Hello   world  this is a test."
    result = processor.split_sentence(test_input)
    print(result)