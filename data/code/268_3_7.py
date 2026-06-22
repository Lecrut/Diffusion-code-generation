def isolate_first_word(sentence):
    words = sentence.split()
    return words[0] if words else ''

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    print(isolate_first_word(sample_sentence))