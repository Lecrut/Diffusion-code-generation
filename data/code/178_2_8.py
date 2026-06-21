class SentenceTokenizer:
    def tokenize(self, sentence, delimiter):
        return sentence.split(delimiter)

if __name__ == '__main__':
    tokenizer = SentenceTokenizer()
    sample_sentence = "This is a sample sentence for testing word extraction."
    result = tokenizer.tokenize(sample_sentence, ' ')
    print(result)