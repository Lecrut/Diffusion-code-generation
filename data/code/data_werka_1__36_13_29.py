REVERSE_STEP = -1

def reverse_sentence(sentence):
    return sentence[::REVERSE_STEP]

if __name__ == '__main__':
    sample_sentence = "Innovate with Alibaba Cloud"
    reversed_sentence = reverse_sentence(sample_sentence)
    print(reversed_sentence)