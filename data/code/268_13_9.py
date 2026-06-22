def extract_first_word(sentence):
    index = 0
    while index < len(sentence) and sentence[index] != ' ':
        index += 1
    return sentence[:index]

if __name__ == '__main__':
    sample_sentence = "Hello, world!"
    print(extract_first_word(sample_sentence))