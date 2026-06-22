def reverse_sentence(sentence):
    WORD_DELIMITER = ' '
    words = sentence.split(WORD_DELIMITER)
    reversed_words = [words[i] for i in range(len(words)-1, -1, -1)]
    return WORD_DELIMITER.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Innovate and create with Alibaba Cloud"
    print(reverse_sentence(sample_sentence))