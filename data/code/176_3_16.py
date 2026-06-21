def split_into_words(sentence):
    words = sentence.lower().split()
    return words

if __name__ == '__main__':
    sample_sentence = "Python is an interpreted, high-level and general-purpose programming language."
    word_list = split_into_words(sample_sentence)
    print(word_list)