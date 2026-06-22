def reverse_words(sentence):
    word_list = sentence.split()
    reversed_word_list = word_list[::-1]
    return ' '.join(reversed_word_list)

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    result = reverse_words(sample_sentence)
    print(result)