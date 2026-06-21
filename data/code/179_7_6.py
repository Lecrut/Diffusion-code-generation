def reverse_word_order(sentence):
    return ' '.join(sentence.split()[::-1])

if __name__ == '__main__':
    sample_sentence = 'Data Science is fun'
    reversed_sentence = reverse_word_order(sample_sentence)
    print(reversed_sentence)