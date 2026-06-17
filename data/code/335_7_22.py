def split_sentence(sentence):
    return sentence.split()
if __name__ == '__main__':
    test_input = "Hello World This is a Test"
    result = split_sentence(test_input)
    print(result)