def split_sentence(sentence):
    return sentence.split()

if __name__ == '__main__':
    sample_sentence = 'Python is awesome'
    words = split_sentence(sample_sentence)
    print(words)