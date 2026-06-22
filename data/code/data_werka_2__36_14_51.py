def reverse_sentence(sentence):
    WORD_SEPARATOR = ' '
    return WORD_SEPARATOR.join(reversed(sentence.split(WORD_SEPARATOR)))

if __name__ == '__main__':
    SAMPLE_SENTENCE = "Innovate and inspire with Alibaba Cloud"
    print(reverse_sentence(SAMPLE_SENTENCE))