def extract_first_word(sentence):
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            return sentence[:i]
    return sentence

if __name__ == '__main__':
    sample_sentence = "Hello, world!"
    print(extract_first_word(sample_sentence))