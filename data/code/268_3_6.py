def validate_sentence(sentence):
    if not isinstance(sentence, str) or sentence.strip() == '':
        raise ValueError("Input must be a non-empty string")

def isolate_first_word(sentence):
    validate_sentence(sentence)
    return sentence.split()[0]

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    print(isolate_first_word(sample_sentence))