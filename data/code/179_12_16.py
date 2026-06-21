def reverse_word_order(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Python is great"
    reversed_sentence = reverse_word_order(sample_sentence)
    print(reversed_sentence)