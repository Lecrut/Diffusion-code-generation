def split_sentence(sentence):
    return sentence.split()
if __name__ == '__main__':
    test_input = "Hello world Python programming"
    result = split_sentence(test_input)
    print(result)