def reverse_words(sentence):
    words_list = sentence.split()
    reversed_list = words_list[::-1]
    result_sentence = ' '.join(reversed_list)
    return result_sentence

if __name__ == '__main__':
    sample_input = "Python is great for coding"
    output = reverse_words(sample_input)
    print(output)