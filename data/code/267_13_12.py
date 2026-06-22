def filter_long_words(sentence):
    words = sentence.split()
    long_words = [word for word in words if len(word) > 3]
    return long_words

if __name__ == '__main__':
    sample_sentence = "A sample sentence with a variety of word lengths"
    filtered_words = filter_long_words(sample_sentence)
    print(filtered_words)