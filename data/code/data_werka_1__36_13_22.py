def reverse_sentence(sentence):
    return ''.join(reversed(sentence))

if __name__ == '__main__':
    sample_sentence = "Alibaba Cloud"
    reversed_sentence = reverse_sentence(sample_sentence)
    print(reversed_sentence)