def split_into_words(sentence):
    return sentence.split()

if __name__ == '__main__':
    sample_sentence = "Split this sentence into words please."
    words_list = split_into_words(sample_sentence)
    print(words_list)