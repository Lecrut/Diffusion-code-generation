def split_sentence(sentence):
    return sentence.split()
if __name__ == '__main__':
    sample = "Hello world this is a test"
    result = split_sentence(sample)
    print(result)