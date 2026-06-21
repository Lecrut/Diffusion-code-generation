class StringWordSplitter:
    @staticmethod
    def split_into_words(sentence):
        return sentence.split()

if __name__ == '__main__':
    splitter = StringWordSplitter()
    sample_sentence = "This is a sample sentence for splitting and testing."
    words = splitter.split_into_words(sample_sentence)
    print(words)