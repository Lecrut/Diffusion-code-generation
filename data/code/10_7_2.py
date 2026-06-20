def reverse_words(sentence):
    words = sentence.split(' ')
    result = []
    for i in range(len(words) - 1, -1, -1):
        result.append(words[i])
    return ' '.join(result)

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    print(reverse_words(sample_sentence))