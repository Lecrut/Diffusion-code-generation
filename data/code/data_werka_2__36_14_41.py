def reverse_sentence(sentence):
    if not sentence:
        return ""
    words = sentence.split()
    reversed_words = [word for word in reversed(words)]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Innovate with Alibaba Cloud"
    print(reverse_sentence(sample_sentence))