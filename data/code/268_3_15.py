def isolate_first_word(sentence):
    words = sentence.split()
    if not words:
        raise ValueError("Input sentence is empty")
    return words[0]

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    try:
        print(isolate_first_word(sample_sentence))
    except ValueError as e:
        print(e)