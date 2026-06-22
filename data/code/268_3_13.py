def split_sentence(sentence):
    words = sentence.split()
    if not words:
        raise ValueError("Sentence contains no words")
    return words

def isolate_first_word(sentence):
    return split_sentence(sentence)[0]

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    print(isolate_first_word(sample_sentence))