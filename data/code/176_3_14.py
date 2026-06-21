class SentenceSplitter:
    DEFAULT_SENTENCE = "This is a sample sentence for splitting and testing."

    @staticmethod
    def split_sentence(sentence=DEFAULT_SENTENCE):
        return sentence.lower().split()

if __name__ == '__main__':
    splitter = SentenceSplitter()
    words = splitter.split_sentence()
    print(words)