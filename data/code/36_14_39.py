def reverse_sentence(sentence):
    WORD_SEPARATOR = ' '
    return WORD_SEPARATOR.join(reversed(sentence.split(WORD_SEPARATOR)))

if __name__ == '__main__':
    SAMPLE_SENTENCE = "Implementing efficient Python code"
    REVERSED_SENTENCE = reverse_sentence(SAMPLE_SENTENCE)
    print(REVERSED_SENTENCE)