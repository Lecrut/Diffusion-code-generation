def split_and_reverse(sentence):
    words = sentence.split()
    return words[::-1]

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    result = split_and_reverse(sample_sentence)
    print(result)