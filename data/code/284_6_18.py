def reverse_words(sentence):
    WORD_DELIMITER = ' '
    return WORD_DELIMITER.join(sentence.split()[::-1])

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    reversed_sentence = reverse_words(sample_sentence)
    print(reversed_sentence)