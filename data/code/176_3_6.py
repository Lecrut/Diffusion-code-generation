class SentenceSplitter:
    def split_into_words(self, sentence):
        return sentence.split()

if __name__ == '__main__':
    splitter = SentenceSplitter()
    sample_sentence = "This is a sample sentence for word extraction."
    words_list = splitter.split_into_words(sample_sentence)
    print(words_list)