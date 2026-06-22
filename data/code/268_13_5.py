def extract_first_word(sentence):
    i = 0
    while i < len(sentence) and sentence[i] != ' ':
        i += 1
    return sentence[:i]

if __name__ == '__main__':
    sample_sentence = "Hello, world!"
    print(extract_first_word(sample_sentence))