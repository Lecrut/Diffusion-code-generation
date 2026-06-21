def tokenize_sentence(sentence, delimiter):
    if not isinstance(sentence, str) or not isinstance(delimiter, str):
        raise ValueError("Both sentence and delimiter must be strings")
    
    return sentence.split(delimiter)

if __name__ == '__main__':
    sample_sentence = "Hello,world,this,is,a,test."
    delimiter = ","
    print(tokenize_sentence(sample_sentence, delimiter))