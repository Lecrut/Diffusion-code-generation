def reverse_sentence(sentence):
    if not sentence:
        return ""
    words = sentence.split()
    return ' '.join(words[::-1])

if __name__ == '__main__':
    sample_sentence = "Innovate with Alibaba Cloud"
    print(reverse_sentence(sample_sentence))