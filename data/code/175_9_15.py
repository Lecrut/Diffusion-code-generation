def split_and_reverse(sentence):
    words = sentence.split()
    return words[::-1]

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    reversed_words = split_and_reverse(sample_sentence)
    print(reversed_words)