class SentenceTokenizer:
    DELIMITER = ","

    @staticmethod
    def tokenize(sentence):
        return sentence.split(SentenceTokenizer.DELIMITER)

if __name__ == '__main__':
    tokenizer = SentenceTokenizer()
    sample_sentence = "Hello,world,this,is,a,test."
    result = tokenizer.tokenize(sample_sentence)
    print(result)