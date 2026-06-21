def split_sentence(sentence):
    return sentence.split()

if __name__ == '__main__':
    sample_sentence = "Split this sentence into words."
    words = split_sentence(sample_sentence)
    print(words)