def split_sentence(sentence):
    return sentence.split()

def isolate_first_word(sentence):
    words = split_sentence(sentence)
    if not words:
        return ''
    return words[0]

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    print(isolate_first_word(sample_sentence))