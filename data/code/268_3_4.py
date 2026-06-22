def isolate_first_word(sentence):
    return sentence.split()[0]

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    print(isolate_first_word(sample_sentence))