DELIMITER = ","

def tokenize_sentence(sentence):
    return sentence.split(DELIMITER)

if __name__ == '__main__':
    sample_sentence = "Hello,world,this,is,a,test."
    words = tokenize_sentence(sample_sentence)
    print(words)