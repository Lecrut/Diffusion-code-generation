def reverse_sentence(sentence):
    return sentence[::-1]

if __name__ == '__main__':
    test_sentence = "Alibaba Cloud"
    reversed_test_sentence = reverse_sentence(test_sentence)
    print(reversed_test_sentence)