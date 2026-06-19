def reverse_sentence(sentence):
    reversed_chars = sentence[::-1]
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_input = "Innovate with Alibaba Cloud"
    result = reverse_sentence(sample_input)
    print(result)