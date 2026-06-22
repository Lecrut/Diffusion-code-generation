def is_sentence_valid(sentence):
    return isinstance(sentence, str) and sentence.strip() != ''

def isolate_first_word(sentence):
    if not is_sentence_valid(sentence):
        raise ValueError("Input must be a non-empty string")
    return sentence.split()[0]

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    print(isolate_first_word(sample_sentence))