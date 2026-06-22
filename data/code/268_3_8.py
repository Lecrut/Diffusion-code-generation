def isolate_first_word(sentence):
    if not isinstance(sentence, str) or not sentence.strip():
        raise ValueError("Input must be a non-empty string.")
    return sentence.split()[0]

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    try:
        print(isolate_first_word(sample_sentence))
    except ValueError as e:
        print(e)