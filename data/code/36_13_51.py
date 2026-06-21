def reverse_sentence_in_place(sentence):

    def reverse_word(word):
        left, right = (0, len(word) - 1)
        while left < right:
            word[left], word[right] = (word[right], word[left])
            left += 1
            right -= 1
    sentence_list = list(sentence)
    start = 0
    for end in range(len(sentence_list)):
        if sentence_list[end] == ' ':
            reverse_word(sentence_list[start:end])
            start = end + 1
    reverse_word(sentence_list[start:])
    reverse_word(sentence_list)
    return ''.join(sentence_list)
if __name__ == '__main__':
    test_sentence = 'Hello World'
    reversed_sentence = reverse_sentence_in_place(test_sentence)
    print(reversed_sentence)