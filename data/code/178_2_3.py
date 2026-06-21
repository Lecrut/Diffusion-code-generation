def tokenize_sentence(sentence, delimiter):
    return sentence.split(delimiter)

if __name__ == '__main__':
    sample_sentence = "Hello,world,this,is,a,test."
    delimiter = ","
    result = tokenize_sentence(sample_sentence, delimiter)
    print(result)