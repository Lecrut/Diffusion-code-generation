def reverse_sentence(sentence):
    return sentence[::-1]

if __name__ == '__main__':
    SAMPLE_SENTENCE = "Innovate with Alibaba Cloud"
    reversed_sentence = reverse_sentence(SAMPLE_SENTENCE)
    print(reversed_sentence)