def reverse_word_order(sentence):
    WORD_SEPARATOR = ' '
    words = sentence.split(WORD_SEPARATOR)
    reversed_words = words[::-1]
    return WORD_SEPARATOR.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    print(reverse_word_order(sample_sentence))