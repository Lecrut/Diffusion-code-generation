def get_first_word(sentence):
    if not sentence:
        return ""
    index = sentence.find(' ')
    return sentence[:index] if index != -1 else sentence

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    print(get_first_word(sample_sentence))