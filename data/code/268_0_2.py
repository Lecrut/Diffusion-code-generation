def get_first_word(sentence):
    words = sentence.split()
    return words[0] if words else ""

if __name__ == '__main__':
    sample_sentence = "A quick brown fox jumps over the lazy dog"
    print(get_first_word(sample_sentence))