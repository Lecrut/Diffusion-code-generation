def reverse_word_order(sentence):
    return ' '.join(sentence.split()[::-1])

if __name__ == '__main__':
    sample_sentence = 'Data Science is fun'
    print(reverse_word_order(sample_sentence))