def extract_first_word(sentence):
    word = ''
    for char in sentence:
        if char == ' ':
            break
        word += char
    return word

if __name__ == '__main__':
    sample_sentence = "Hello world, this is a test."
    print(extract_first_word(sample_sentence))