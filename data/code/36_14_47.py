def reverse_sentence(sentence):
    WORD_SEPARATOR = ' '
    return WORD_SEPARATOR.join(sentence.split(WORD_SEPARATOR)[::-1])

if __name__ == '__main__':
    SAMPLE_SENTENCE = "Implement an efficient Python function"
    print(reverse_sentence(SAMPLE_SENTENCE))