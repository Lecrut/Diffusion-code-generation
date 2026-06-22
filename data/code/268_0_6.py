def find_first_word(sentence):
    return sentence.split()[0]

if __name__ == '__main__':
    sample_sentence = "Python is great"
    print(find_first_word(sample_sentence))