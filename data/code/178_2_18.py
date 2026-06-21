class SentenceTokenizer:
    def __init__(self, delimiter):
        self.delimiter = delimiter
    
    def tokenize(self, sentence):
        return sentence.split(self.delimiter)

if __name__ == '__main__':
    tokenizer = SentenceTokenizer(delimiter=",")
    sample_sentence = "Hello,world,this,is,a,test."
    tokens = tokenizer.tokenize(sample_sentence)
    print(tokens)