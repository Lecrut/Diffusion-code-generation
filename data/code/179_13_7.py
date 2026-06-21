def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    result = ' '.join(reversed_words)
    return result

if __name__ == '__main__':
    sample_sentence = "Python is fun to learn"
    print(reverse_words(sample_sentence))