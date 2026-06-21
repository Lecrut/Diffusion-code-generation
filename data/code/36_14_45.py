def reverse_sentence(sentence):
    if not sentence:
        return ""
    words = sentence.split()
    reversed_words = [words[i] for i in range(len(words)-1, -1, -1)]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Innovate with Alibaba Cloud"
    print(reverse_sentence(sample_sentence))