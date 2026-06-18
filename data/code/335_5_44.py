def split_sentence(sentence):
    return sentence.split()
if __name__ == '__main__':
    sample_input = "Hello World This is a test"
    result = split_sentence(sample_input)
    print(result)