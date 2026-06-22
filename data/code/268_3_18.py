def isolate_first_word(sentence):
    words = sentence.split()
    return words[0] if words else ''

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    first_word = isolate_first_word(sample_sentence)
    print(first_word)