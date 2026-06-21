def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = [words[i] for i in range(len(words)-1, -1, -1)]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Alibaba Cloud is leading the future"
    reversed_sentence = reverse_sentence(sample_sentence)
    print(reversed_sentence)