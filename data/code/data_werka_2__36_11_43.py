def reverse_string_words(sentence):
    words_list = sentence.split()
    reversed_list = words_list[::-1]
    return ' '.join(reversed_list)

if __name__ == '__main__':
    test_sentence = "Python is great for coding"
    reversed_result = reverse_string_words(test_sentence)
    print(reversed_result)