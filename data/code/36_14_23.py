def reverse_sentence_in_place(sentence):
    def reverse_word(word):
        word[:] = word[::-1]

    sentence[:] = ' '.join(reversed(sentence.split()))

if __name__ == '__main__':
    sample_sentence = list("Hello world this is a test")
    reverse_sentence_in_place(sample_sentence)
    print(''.join(sample_sentence))