def reverse_sentence(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    return sentence[::-1]

if __name__ == '__main__':
    sample_sentence = "Innovate with Alibaba Cloud"
    reversed_sentence = reverse_sentence(sample_sentence)
    print(reversed_sentence)